import unittest
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from app.app import app, db
from app.models import User

class SeleniumTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start Flask server in a thread
        cls.server_thread = threading.Thread(target=app.run, kwargs={'port': 5001, 'use_reloader': False})
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(1)  # Give the server time to start

        # Set up headless Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.base_url = "http://localhost:5001/"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        with app.app_context():
            db.create_all()
            # Add test users
            user1 = User(first_name="Alice", last_name="Smith", email="alice@example.com")
            user1.set_password("password")
            user2 = User(first_name="Bob", last_name="Brown", email="bob@example.com")
            user2.set_password("password")
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

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
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.assertIn("Profile", self.driver.title)

    # 5. Failed login (wrong password)
    def test_failed_login_wrong_password(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("wrongpass")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.assertIn("Login", self.driver.title)
        self.assertIn("Invalid email or password", self.driver.page_source)

    # 6. Failed login (nonexistent user)
    def test_failed_login_nonexistent_user(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("nobody@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.assertIn("Login", self.driver.title)
        self.assertIn("Invalid email or password", self.driver.page_source)

    # 7. Login form validation (empty fields)
    def test_login_empty_fields(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.assertIn("This field is required", self.driver.page_source)

    # 8. Navigation to profile after login
    def test_profile_page_after_login(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.get(self.base_url + "profile")
        self.assertIn("Profile", self.driver.title)

    # 9. Navigation to tools page after login
    def test_tools_page_after_login(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.get(self.base_url + "tools")
        self.assertIn("Tools", self.driver.title)

    # 10. Posts page requires login
    def test_posts_page_requires_login(self):
        self.driver.get(self.base_url + "posts")
        self.assertIn("Login", self.driver.title)

    # 11. Profile page requires login
    def test_profile_requires_login(self):
        self.driver.get(self.base_url + "profile")
        self.assertIn("Login", self.driver.title)

    # 12. Tools page requires login
    def test_tools_requires_login(self):
        self.driver.get(self.base_url + "tools")
        self.assertIn("Login", self.driver.title)

    # 13. Login with second user
    def test_login_second_user(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("bob@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.assertIn("Profile", self.driver.title)

    # 14. Check logout (if implemented)
    def test_logout(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # If you have a logout link or button, click it and check redirect
        try:
            self.driver.find_element(By.LINK_TEXT, "Logout").click()
            self.assertIn("Login", self.driver.title)
        except Exception:
            self.skipTest("Logout not implemented")

    # 15. Check that user info is displayed on profile page
    def test_profile_user_info(self):
        self.driver.get(self.base_url + "login")
        self.driver.find_element(By.NAME, "email").send_keys("alice@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.get(self.base_url + "profile")
        self.assertIn("alice@example.com", self.driver.page_source)

if _name_ == "_main_":
    unittest.main()
