# backend/auth.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User

auth_bp = Blueprint('auth', __name__)
users_db = {}  # Temporary in-memory database

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users_db:
        return jsonify({'message': 'User already exists'}), 400

    user = User(username, password)
    users_db[username] = user
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users_db.get(username)
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify({'token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401
