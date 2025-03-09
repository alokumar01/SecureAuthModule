from flask import Flask
from config import Config
from auth.routes import auth_blueprint
from database.db import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
jwt = JWTManager(app)
db.init_app(app)

# Register Blueprints (Authentication Routes)
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# Test Route
@app.route('/')
def home():
    return "Secure Authentication Module is Running!"

if __name__ == '__main__':
    app.run(debug=True)
