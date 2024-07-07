from flask import Blueprint, request, jsonify
from models import db, User
from utils.jwt import generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    """
    Sign up a new user.
    
    Returns:
        Response: A JSON response indicating success or failure.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "User created successfully"}), 201
        return jsonify({"error": "Invalid input"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Log in an existing user.
    
    Returns:
        Response: A JSON response with a JWT token if successful.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            token = generate_token(user.id)
            return jsonify({"token": token}), 200
        return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
