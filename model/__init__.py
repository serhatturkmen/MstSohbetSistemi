from flask_sqlalchemy import SQLAlchemy
from dateFunctions import getdate

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.Text)
    surname = db.Column(db.Text)
    status = db.Column(db.Integer)
    imagePath = db.Column(db.Text)
    gender = db.Column(db.Text, default="E")
    email = db.Column(db.Text, unique=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    createdDate = db.Column(db.Text, default=getdate())
    lastSeenDate = db.Column(db.Text, default=getdate())
    userAccept = db.Column(db.Boolean, default=False)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    roomId = db.Column(db.Text)
    userId = db.Column(db.Integer)
    messageContent = db.Column(db.Text)
    messageDate = db.Column(db.Text, default=getdate())


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    user1 = db.Column(db.Integer)
    user2 = db.Column(db.Integer)


class WebSetting(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    title = db.Column(db.String(180))
    metaKeyword = db.Column(db.Text)
    metaTitle = db.Column(db.Text)
    icon = db.Column(db.Text)
    analytics = db.Column(db.Text)


class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    smtpServer = db.Column(db.Text)
    smtpEmail = db.Column(db.Text)
    smtpPassword = db.Column(db.Text)
    smtpPort = db.Column(db.Integer)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    tokenId = db.Column(db.Text)
    processDate = db.Column(db.Text, default=getdate())
    process = db.Column(db.Text)
    status = db.Column(db.Boolean, default=False)
    userId = db.Column(db.Integer)
