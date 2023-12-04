from flask import Flask


app = Flask(__name__)


from routes import user_routes
from routes import admin_routes
