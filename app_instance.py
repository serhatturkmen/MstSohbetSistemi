from flask import Flask
from flask_socketio import SocketIO
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, ASYNC_MODE
from model import db

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

socketio = SocketIO(app, async_mode=ASYNC_MODE)

db.init_app(app)

with app.app_context():
    db.create_all()

