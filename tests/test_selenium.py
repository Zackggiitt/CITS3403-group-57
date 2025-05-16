import unittest
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.app import create_app, db
from config import TestingConfig
from app.models import User

class SeleniumTestCase(unittest.TestCase):
    flask_app = None
    app_context = None
    server_thread = None
    driver = None
    base_url = "http://localhost:5001/"

    @classmethod
    def setUpClass(cls):
        # Create Flask app instance using TestingConfig
        cls.flask_app = create_app(TestingConfig)
        cls.app_context = cls.flask_app.app_context()
        cls.app_context.push()

        # Create database tables ONCE for the class
        db.create_all()
        # DO NOT add general users here; this will be done in setUp (method level)

        # Start Flask server in a thread with the created app instance
        cls.server_thread = threading.Thread(target=cls.flask_app.run, kwargs={'host': '0.0.0.0', 'port': 5001, 'use_reloader': False, 'debug': False})
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(2)  # Give the server more time to start

        # Set up headless Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        try:
            cls.driver = webdriver.Chrome(options=chrome_options)
        except Exception as e:
            print(f"Error initializing WebDriver: {e}")
            if cls.app_context: # Ensure context might have been pushed
                 cls.app_context.pop()
            raise

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()
        
        if cls.app_context:
            db.session.remove() # Ensure session is clean before dropping
            db.drop_all()       # Drop all tables ONCE for the class
            cls.app_context.pop()

    def _clear_db_data(self):
        # Helper to clear data from all tables
        # Ensures it runs within the application context established by setUpClass
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

    def setUp(self):
        # This runs before each test method
        self._clear_db_data() # Clear data from previous test

        # Add common/specific test users for this test method
        # These users are created fresh for each test method
        user1 = User(first_name="Alice", last_name="Smith", email="alice@example.com")
        user1.set_password("password")
        user2 = User(first_name="Bob", last_name="Brown", email="bob@example.com")
        user2.set_password("password")
        db.session.add_all([user1, user2])
        db.session.commit()

        if self.driver:
             self.driver.delete_all_cookies()
             self.driver.get("about:blank") # Navigate to a blank page first
             time.sleep(0.1) # Short pause to ensure blank page is loaded if needed
             self.driver.get(self.base_url + "login")

    def tearDown(self):
        # This runs after each test method
        self._clear_db_data() # Clear data after test execution

    # 1. Home page loads
    def test_homepage_loads(self):
        self.driver.get(self.base_url)
        self.assertIn("Home", self.driver.title)

    # 2. Login page loads
    def test_login_page_loads(self):
        self.driver.get(self.base_url + "login")
        self.assertIn("Login", self.driver.title)

    # 3. Login form present
    def test_login_form_present(self):
        self.driver.get(self.base_url + "login")
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        self.assertIsNotNone(email_input)
        self.assertIsNotNone(password_input)

    # NEW TEST: Successful login
    def test_successful_login(self):
        self.driver.get(self.base_url + "login")
        print(f"[SELENIUM_DEBUG] Navigated to: {self.driver.current_url}, Title: {self.driver.title}")

        email_field = self.driver.find_element(By.NAME, "email")
        password_field = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_field.send_keys("alice@example.com")
        password_field.send_keys("password")
        print(f"[SELENIUM_DEBUG] Credentials entered.")
        submit_button.click()
        print(f"[SELENIUM_DEBUG] Submit button clicked.")

        try:
            # Wait for the URL to change to /profile (or contain /profile)
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/profile")
            )
            print(f"[SELENIUM_DEBUG] Redirected to: {self.driver.current_url}, Title: {self.driver.title}")
            # Assert that the title of the page is Profile, indicating successful login and redirect
            self.assertIn("Profile", self.driver.title, "Login failed or did not redirect to profile page title.")
            self.assertTrue(self.driver.current_url.endswith("/profile"), "URL did not end with /profile")
        except Exception as e:
            print(f"[SELENIUM_DEBUG] Exception after login attempt: {e}")
            print(f"[SELENIUM_DEBUG] Current URL: {self.driver.current_url}")
            print(f"[SELENIUM_DEBUG] Current Title: {self.driver.title}")
            print(f"[SELENIUM_DEBUG] Page Source (first 500 chars): {self.driver.page_source[:500]}")
            self.fail(f"Login failed. Current URL: {self.driver.current_url}, Title: {self.driver.title}. Exception: {e}")

    # 5. Failed login (wrong password)
    def test_failed_login_wrong_password(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("wrongpass")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(0.5)
        self.assertIn("Login", self.driver.title) # Should remain on login page
        self.assertIn("Invalid email or password", self.driver.page_source)

    # 6. Failed login (nonexistent user)
    def test_failed_login_nonexistent_user(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("nobody@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(0.5)
        self.assertIn("Login", self.driver.title) # Should remain on login page
        self.assertIn("Invalid email or password", self.driver.page_source)

    # 10. Posts page requires login
    def test_posts_page_requires_login(self):
        self.driver.get(self.base_url + "posts") # Accessing directly without login
        time.sleep(0.5)
        self.assertIn("Login", self.driver.title) # Should be redirected to login

    # 11. Profile page requires login
    def test_profile_requires_login(self):
        # Cookies are cleared in setUp, so this effectively tests unauthenticated access
        self.driver.get(self.base_url + "profile")
        time.sleep(0.5)
        self.assertIn("Login", self.driver.title)

    # 12. Tools page requires login
    def test_tools_requires_login(self):
        self.driver.get(self.base_url + "tools")
        time.sleep(0.5)
        self.assertIn("Login", self.driver.title)

    # 13. Login with second user
    def test_login_second_user(self):
        self.driver.get(self.base_url + "login")
        email_field = self.driver.find_element(By.NAME, "email")
        password_field = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_field.send_keys("bob@example.com")
        password_field.send_keys("password")
        submit_button.click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/profile")
            )
            # Assert that the title of the page is Profile, indicating successful login and redirect
            self.assertIn("Profile", self.driver.title, "Login with Bob failed or did not redirect to profile page title.")
            self.assertTrue(self.driver.current_url.endswith("/profile"), "URL (Bob login) did not end with /profile")
        except Exception as e:
            # Adding more debug info similar to test_successful_login
            print(f"[SELENIUM_DEBUG] Exception during Bob login: {e}")
            print(f"[SELENIUM_DEBUG] Current URL (Bob login): {self.driver.current_url}")
            print(f"[SELENIUM_DEBUG] Current Title (Bob login): {self.driver.title}")
            print(f"[SELENIUM_DEBUG] Page Source (Bob login) (first 500 chars): {self.driver.page_source[:500]}")
            self.fail(f"Login with Bob failed. Current URL: {self.driver.current_url}, Title: {self.driver.title}. Exception: {e}")

    # 14. Check logout
    def test_logout(self):
        # 1. Log in user (Alice)
        self.driver.get(self.base_url + "login")
        email_field = self.driver.find_element(By.NAME, "email")
        password_field = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_field.send_keys("alice@example.com")
        password_field.send_keys("password")
        submit_button.click()

        # 2. Wait for successful login and redirect to profile page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/profile")
            )
            # Optional: Check title as well if desired
            # self.assertIn("Profile", self.driver.title, "Login failed or did not redirect to profile page before logout attempt.")
        except Exception as e:
            self.fail(f"Login as Alice failed before logout attempt. Current URL: {self.driver.current_url}, Title: {self.driver.title}. Exception: {e}")

        # 3. Find and click the logout link
        try:
            # Assuming logout link is identifiable by its text or a more specific selector
            # If the link text/selector changes, this needs to be updated.
            logout_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
            )
            logout_link.click()
        except Exception as e:
            self.fail(f"Logout link not found or could not be clicked. Exception: {e}")

        # 4. Wait for successful logout and redirect to login page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/login") # After logout, should be back to login page
            )
            self.assertIn("Login", self.driver.title, "Logout failed or did not redirect to login page.")
            # Ensure we are on the login page URL, not just a page with "Login" in title that might be an error page
            self.assertTrue(self.driver.current_url.endswith("/login"), "After logout, URL did not end with /login")
        except Exception as e:
            self.fail(f"Redirection to login page after logout failed. Current URL: {self.driver.current_url}, Title: {self.driver.title}. Exception: {e}")

    # Test for accessing profile page after login
    def test_profile_page_after_login(self):
        # 1. Log in user (Alice)
        self.driver.get(self.base_url + "login")
        email_field = self.driver.find_element(By.NAME, "email")
        password_field = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_field.send_keys("alice@example.com")
        password_field.send_keys("password")
        submit_button.click()

        # 2. Wait for successful login and redirect to profile page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/profile")
            )
            self.assertIn("Profile", self.driver.title, "Did not redirect to profile page title after login.")
            self.assertTrue(self.driver.current_url.endswith("/profile"), "URL did not end with /profile after login.")
        except Exception as e:
            self.fail(f"Login as Alice failed when testing profile page access. Current URL: {self.driver.current_url}, Title: {self.driver.title}. Exception: {e}")
        
        # 3. Verify profile page content (e.g., user's name)
        # This assumes the user's first name is displayed on the profile page.
        # Adjust the selector and text if necessary based on your app's HTML structure.
        try:
            # Example: Wait for an element that contains the user's first name "Alice"
            # This is a placeholder; a more specific selector (e.g., by ID or class) is better.
            user_name_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Alice')]")) 
            )
            self.assertIn("Alice", user_name_element.text, "User's first name not found on profile page.")
            # You might also want to check for last name or email if they are displayed.
        except Exception as e:
            self.fail(f"Failed to verify content on profile page for Alice. Exception: {e}\nPage Source (first 500 chars): {self.driver.page_source[:500]}")

    # Test for accessing tools page after login
    def test_tools_page_after_login(self):
        # 1. Log in user (Alice)
        self.driver.get(self.base_url + "login")
        email_field = self.driver.find_element(By.NAME, "email")
        password_field = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_field.send_keys("alice@example.com")
        password_field.send_keys("password")
        submit_button.click()

        # 2. Wait for successful login (redirects to profile first by default)
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("/profile"))
        except Exception as e:
            self.fail(f"Login as Alice failed before attempting to navigate to tools page. Current URL: {self.driver.current_url}, Title: {self.driver.title}. Exception: {e}")

        # 3. Navigate to the tools page
        self.driver.get(self.base_url + "tools")

        # 4. Wait for the tools page to load and verify
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("/tools"))
            self.assertIn("Tools", self.driver.title, "Did not navigate to tools page title after login.")
            self.assertTrue(self.driver.current_url.endswith("/tools"), "URL did not end with /tools after navigation.")
        except Exception as e:
            self.fail(f"Failed to access or verify tools page after login. Current URL: {self.driver.current_url}, Title: {self.driver.title}. Exception: {e}")

if __name__ == "__main__":
    unittest.main()
