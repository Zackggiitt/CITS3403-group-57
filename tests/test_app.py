import unittest
from app.app import create_app, db
from config import TestingConfig
from app.models import User, WorkoutPlan, SharedPlan
from werkzeug.security import generate_password_hash
from datetime import datetime

class TestUserModel(unittest.TestCase):
    def setUp(self):
        # Create Flask app instance using TestingConfig
        self.flask_app = create_app(TestingConfig)
        self.app_context = self.flask_app.app_context()
        self.app_context.push()
        self.app = self.flask_app.test_client()
        
        # Create database tables within the app context
        db.create_all()
            
        # Create a test user
        self.test_user = User(
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        self.test_user.set_password('password123')
        
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        """Test 1: Test password hashing and verification"""
        user = User.query.filter_by(email='test@example.com').first()
        self.assertTrue(user.check_password('password123'))
        self.assertFalse(user.check_password('wrongpassword'))

    def test_password_hashing_different_users(self):
        """Test 2: Test password hashing for different users"""
        user1 = User(email='user1@test.com', first_name='User1', last_name='Test')
        user2 = User(email='user2@test.com', first_name='User2', last_name='Test')
        
        user1.set_password('password123')
        user2.set_password('password123')
        
        # Even with same password, hashes should be different due to salting
        self.assertNotEqual(user1.password_hash, user2.password_hash)

    def test_user_to_dict(self):
        """Test 3: Test user to dictionary conversion"""
        user = User.query.filter_by(email='test@example.com').first()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], 'test@example.com')
        self.assertEqual(user_dict['first_name'], 'Test')
        self.assertEqual(user_dict['last_name'], 'User')
        self.assertTrue('id' in user_dict)

    def test_invalid_password_type(self):
        """Test 4: Test setting invalid password type"""
        user = User(email='test2@test.com', first_name='Test2', last_name='User')
        with self.assertRaises(TypeError):
            user.set_password(None)


class TestLoginRoute(unittest.TestCase):
    def setUp(self):
        self.flask_app = create_app(TestingConfig)
        self.app_context = self.flask_app.app_context()
        self.app_context.push()
        self.app = self.flask_app.test_client()
        
        db.create_all()
        # Create test user
        user = User(
            email='test@example.com',
            first_name='Test',
            last_name='User'
        )
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_login_success(self):
        """Test 1: Test successful login"""
        response = self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged in successfully', response.data)
        self.assertIn(b'Profile', response.data)

    def test_login_wrong_password(self):
        """Test 2: Test login with wrong password"""
        response = self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        self.assertIn(b'Invalid email or password', response.data)

    def test_login_nonexistent_user(self):
        """Test 3: Test login with non-existent user"""
        response = self.app.post('/login', data={
            'email': 'nonexistent@example.com',
            'password': 'password123'
        }, follow_redirects=True)
        self.assertIn(b'Invalid email or password', response.data)

    def test_login_empty_fields(self):
        """Test 4: Test login with empty fields"""
        response = self.app.post('/login', data={
            'email': '',
            'password': ''
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email and password are required', response.data)


class TestWorkoutPlanSharing(unittest.TestCase):
    def setUp(self):
        self.flask_app = create_app(TestingConfig)
        self.app_context = self.flask_app.app_context()
        self.app_context.push()
        self.app = self.flask_app.test_client()
        
        db.create_all()
        
        # Create two test users
        self.user1 = User(
            email='user1@example.com',
            first_name='User1',
            last_name='Test'
        )
        self.user1.set_password('password123')
        
        self.user2 = User(
            email='user2@example.com',
            first_name='User2',
            last_name='Test'
        )
        self.user2.set_password('password123')
        
        db.session.add(self.user1)
        db.session.add(self.user2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def _login(self, email, password):
        return self.app.post('/login', data={'email': email, 'password': password}, follow_redirects=True)

    def test_share_plan_success(self):
        """Test 1: Test successful plan sharing"""
        self._login('user1@example.com', 'password123')
        
        response = self.app.post('/api/share_plan', 
            json={'recipientEmail': 'user2@example.com'},
            content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Plan shared successfully', response.data)
        
        shared_plan = SharedPlan.query.filter_by(sharer_id=self.user1.id, recipient_id=self.user2.id).first()
        self.assertIsNotNone(shared_plan)

    def test_share_plan_with_self(self):
        """Test 2: Test sharing plan with self"""
        self._login('user1@example.com', 'password123')
        
        response = self.app.post('/api/share_plan', 
            json={'recipientEmail': 'user1@example.com'},
            content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'You cannot share a plan with yourself.', response.data)

    def test_share_plan_nonexistent_user(self):
        """Test 3: Test sharing plan with non-existent user"""
        self._login('user1@example.com', 'password123')
        
        response = self.app.post('/api/share_plan', 
            json={'recipientEmail': 'nonexistent@example.com'},
            content_type='application/json')
        
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'not found', response.data)

    def test_share_plan_invalid_request(self):
        """Test 4: Test sharing plan with invalid request format"""
        self._login('user1@example.com', 'password123')
        
        response = self.app.post('/api/share_plan', 
            json={},
            content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Missing recipientEmail', response.data)


if __name__ == '__main__':
    unittest.main()
