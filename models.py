from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Product(db.Model):
    """
    Model for the Product table.
    """
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    review_count = db.Column(db.Integer, nullable=True)

class User(db.Model):
    """
    Model for the User table.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """
        Set the password for the user.
        Args:
            password (str): The user's password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check the user's password.
        Args:
            password (str): The user's password.
        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)
