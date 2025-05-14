import unittest
from app.app import app, db
from app.models import User, WorkoutPlan, SharedPlan
from werkzeug.security import generate_password_hash
from datetime import datetime

class TestUserModel(unittest.TestCase):
    def setUp(self):
        # Configure the app for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        
        # Create database tables
        with app.app_context():
            db.create_all()
            
        # Create a test user
        self.test_user = User(
            first_name='Test',
            last_name='User',
            email='test@example.com'
        )
        self.test_user.set_password('password123')
        
        with app.app_context():
            db.session.add(self.test_user)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_password_hashing(self):
        """Test 1: Test password hashing and verification"""
        with app.app_context():
            user = User.query.filter_by(email='test@example.com').first()
            self.assertTrue(user.check_password('password123'))
            self.assertFalse(user.check_password('wrongpassword'))

    def test_password_hashing_different_users(self):
        """Test 2: Test password hashing for different users"""
        with app.app_context():
            user1 = User(email='user1@test.com', first_name='User1', last_name='Test')
            user2 = User(email='user2@test.com', first_name='User2', last_name='Test')
            
            user1.set_password('password123')
            user2.set_password('password123')
            
            # Even with same password, hashes should be different
            self.assertNotEqual(user1.password_hash, user2.password_hash)

    def test_user_to_dict(self):
        """Test 3: Test user to dictionary conversion"""
        with app.app_context():
            user_dict = self.test_user.to_dict()
            self.assertEqual(user_dict['email'], 'test@example.com')
            self.assertEqual(user_dict['first_name'], 'Test')
            self.assertEqual(user_dict['last_name'], 'User')
            self.assertTrue('id' in user_dict)

    def test_invalid_password_type(self):
        """Test 4: Test setting invalid password type"""
        with app.app_context():
            user = User(email='test2@test.com', first_name='Test2', last_name='User')
            with self.assertRaises(TypeError):
                user.set_password(None)


class TestLoginRoute(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        
        with app.app_context():
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
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_success(self):
        """Test 1: Test successful login"""
        response = self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged in successfully', response.data)

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
        self.assertIn(b'This field is required', response.data)


class TestWorkoutPlanSharing(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        
        with app.app_context():
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
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_share_plan_success(self):
        """Test 1: Test successful plan sharing"""
        with app.app_context():
            # Login as user1
            self.app.post('/login', data={
                'email': 'user1@example.com',
                'password': 'password123'
            })
            
            # Share plan with user2
            response = self.app.post('/api/share_plan', 
                json={'recipientEmail': 'user2@example.com'},
                content_type='application/json')
            
            self.assertEqual(response.status_code, 201)
            self.assertIn(b'Plan shared successfully', response.data)

    def test_share_plan_with_self(self):
        """Test 2: Test sharing plan with self"""
        with app.app_context():
            # Login as user1
            self.app.post('/login', data={
                'email': 'user1@example.com',
                'password': 'password123'
            })
            
            # Try to share plan with self
            response = self.app.post('/api/share_plan', 
                json={'recipientEmail': 'user1@example.com'},
                content_type='application/json')
            
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'cannot share a plan with yourself', response.data)

    def test_share_plan_nonexistent_user(self):
        """Test 3: Test sharing plan with non-existent user"""
        with app.app_context():
            # Login as user1
            self.app.post('/login', data={
                'email': 'user1@example.com',
                'password': 'password123'
            })
            
            # Try to share plan with non-existent user
            response = self.app.post('/api/share_plan', 
                json={'recipientEmail': 'nonexistent@example.com'},
                content_type='application/json')
            
            self.assertEqual(response.status_code, 404)
            self.assertIn(b'not found', response.data)

    def test_share_plan_invalid_request(self):
        """Test 4: Test sharing plan with invalid request format"""
        with app.app_context():
            # Login as user1
            self.app.post('/login', data={
                'email': 'user1@example.com',
                'password': 'password123'
            })
            
            # Send invalid request (missing recipientEmail)
            response = self.app.post('/api/share_plan', 
                json={},
                content_type='application/json')
            
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Missing recipientEmail', response.data)


if __name__ == '__main__':
    unittest.main()
