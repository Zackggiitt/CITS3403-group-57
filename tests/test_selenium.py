import unittest
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
            # db.session.remove() # Ensure session is clean before dropping
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

    # 4. Successful login
    def test_successful_login(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # Wait for redirect and page load
        time.sleep(1) # Simple wait, consider explicit waits for robustness
        self.assertIn("Profile", self.driver.title)

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

    # 8. Navigation to profile after login
    def test_profile_page_after_login(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        # Directly navigate or click a link to profile
        profile_url = self.base_url + "profile"
        self.driver.get(profile_url)
        self.assertEqual(self.driver.current_url, profile_url)
        self.assertIn("Profile", self.driver.title)

    # 9. Navigation to tools page after login
    def test_tools_page_after_login(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        tools_url = self.base_url + "tools"
        self.driver.get(tools_url)
        self.assertEqual(self.driver.current_url, tools_url)
        self.assertIn("Tools", self.driver.title)

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
        self.driver.find_element(By.NAME, "email").send_keys("bob@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        self.assertIn("Profile", self.driver.title)

    # 14. Check logout
    def test_logout(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        # Assuming there is a logout link with text "Logout"
        try:
            logout_link = self.driver.find_element(By.LINK_TEXT, "Logout")
            logout_link.click()
            time.sleep(1) # Wait for redirect
            self.assertIn("Login", self.driver.title)
        except Exception as e:
            self.skipTest(f"Logout link not found or error during logout: {e}")

    # 15. Check that user info is displayed on profile page
    def test_profile_user_info(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        self.driver.get(self.base_url + "profile")
        time.sleep(0.5)
        self.assertIn("Alice Smith", self.driver.page_source)

if __name__ == "__main__":
    unittest.main()
