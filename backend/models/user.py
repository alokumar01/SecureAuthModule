# # backend/models/user.py
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

#     def check_password(self, password):
#         return bcrypt.check_password_hash(self.password_hash, password)
