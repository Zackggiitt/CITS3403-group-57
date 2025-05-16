from flask import Flask, Blueprint
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Instantiate extensions globally
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()

# Import database models (must be after db instantiation but before app-specific setup in create_app)
# Models might need db object, but not the app itself yet.
# Adjusted for direct import within the package
from . import models # This assumes models.py is in the same 'app' package.

# Define the main blueprint
main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')

# --- User Loader Callback for Flask-Login (associated with login_manager) ---
# This callback is used to reload the user object from the user ID stored in the session.
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))

def create_app(config_class=Config):
    app = Flask(__name__,
                template_folder="templates", 
                static_folder="static",
                instance_relative_config=True,
                instance_path=os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'instance'))
    
    app.config.from_object(config_class)

    # Initialize extensions with the app instance
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    login_manager.login_view = 'main.login' # Adjusted for blueprint
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "info"

    # OpenAI API Key Setup
    if app.config.get("OPENAI_API_KEY"):
        openai.api_key = app.config.get("OPENAI_API_KEY")
    else:
        app.logger.warning("OPENAI_API_KEY not set in config. Chatbot functionality might be affected.")

    # Import routes here to avoid circular dependencies with main_bp
    from . import routes 
    app.register_blueprint(main_bp)
    
    # Ensure the instance folder exists
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
        
    # Configure secret key
    app.secret_key = app.config.get('SECRET_KEY', os.environ.get("FLASK_SECRET_KEY"))

    # Add CLI command to initialize database
    @app.cli.command("init-db")
    def init_db_command():
        """Initialize the database."""
        with app.app_context(): # Ensure app context for db operations
            db.create_all()
        print("Initialized the database.")

    return app 