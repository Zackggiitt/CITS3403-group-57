import os
from dotenv import load_dotenv

# Get the absolute path of the directory containing the current file
basedir = os.path.abspath(os.path.dirname(__file__))
# Load environment variables from the .env file in the project root
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # Load SECRET_KEY from environment variables, provide a default for safety (but don't rely on it in production)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Load database URI from environment variables or set a default SQLite path in the instance folder
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app', 'instance', 'app.db') # Default also points to instance folder
    # Disable Flask-SQLAlchemy event system if not used to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Ensure the instance folder exists
    INSTANCE_FOLDER_PATH = os.path.join(basedir, 'app', 'instance')
    if not os.path.exists(INSTANCE_FOLDER_PATH):
        os.makedirs(INSTANCE_FOLDER_PATH)
    
    # OpenAI API Key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # In-memory SQLite database for tests
    WTF_CSRF_ENABLED = False # Disable CSRF forms protection in testing
    SECRET_KEY = 'test-secret-key' # Add a specific secret key for testing