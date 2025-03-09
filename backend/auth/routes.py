from flask import Blueprint, request, jsonify
from database.db import db
from auth.models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity



auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # ✅ Ensure all required fields are present
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    # ✅ Check if user already exists
    existing_user = User.query.filter((User.username == data['username']) | (User.email == data['email'])).first()
    if existing_user:
        return jsonify({'error': 'Username or email already exists'}), 409  # HTTP 409: Conflict

    # ✅ Create and save the new user
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201






@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    

    user = User.query.filter_by(email=data['email']).first()  # ✅ Use email instead of username

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify({'message': 'Login successful', 'access_token': access_token }), 200
    return jsonify({'error': 'Invalid credentials'}), 401



@auth_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello, {current_user}! You have access.'}), 200
