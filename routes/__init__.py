from flask import Flask


app = Flask(__name__,
            template_folder='../templates',
            static_folder='../assets',
            static_url_path='/assets')


from routes import user_routes
from routes import admin_routes
