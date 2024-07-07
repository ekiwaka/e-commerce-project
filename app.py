from flask import Flask
from config import Config
from models import db
from routes.auth import auth_bp
from routes.data import data_bp
from routes.report import report_bp

def create_app():
    """
    Create and configure the Flask application.

    Returns:
        app (Flask): The configured Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(data_bp, url_prefix='/data')
    app.register_blueprint(report_bp, url_prefix='/report')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
