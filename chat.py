from flask import Flask, session, flash, redirect, url_for
from controller import controllerBlueprint
from model import db, chatEvents
from flask_socketio import SocketIO, emit, join_room, leave_room
from dateFunctions import getdate
from emoji import emojize


app = Flask(__name__)
app.config['SECRET_KEY'] = 'qweytsdsar__*?.a32||klmbrd'

app.register_blueprint(controllerBlueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veritabani.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

siteurl = 'http://127.0.0.1:5050'

async_mode = 'threading'
socketio = SocketIO(app, async_mode=async_mode)

kullanicilar=list()


@socketio.on('joined', namespace='/chat')
def joined(message):
    if session.get("login", ""):
        room = session.get("chatid", "")
        name = session.get("name", "")
        if name in kullanicilar:
            join_room(room)
            emit('users', {'user': kullanicilar}, room=room)
        else:
            join_room(room)
            kullanicilar.append(name)
            emit('users', {'user': kullanicilar}, room=room, broadcast=True)
    else:
        flash('Giriş Bulunamadı', 'danger')
        return redirect(url_for('.login'))


@socketio.on('text', namespace='/chat')
def text(message):
    if session.get("login", ""):
        # gelen mesaj içeriğini odadaki kullanıcılara gönderiyor.
        room = session.get("chatid", "")
        # türkçe karakter sorunu
        # mesaj = message['msg'].encode('latin-1').decode('utf-8')
        mesaj = message['msg']
        userid = session.get("userid", "")
        emit('message', {'msg': emojize(mesaj), 'userid': userid, 'tarih': getdate()}, room=room, broadcast=False)
        chatEvents.addmessage(
            roomid=room,
            userid=session.get("userid", ""),
            messagecontent=mesaj,
            messagedate=str(getdate())
        )
    else:
        flash('Giriş Bulunamadı', 'danger')
        return redirect(url_for('.login'))


@socketio.on('left', namespace='/chat')
def left(message):
    if session.get("login", ""):
        room = session.get("chatid", "")
        name = session.get("name", "")
        leave_room(room)
        kullanicilar.remove(name)
        emit('users', {'user': kullanicilar}, room=room)
    else:
        flash('Giriş Bulunamadı', 'danger')
        return redirect(url_for('.login'))


if __name__ == '__main__':
    # first use
    # socketio.run(app, port=5050, debug=True, host="192.168.1.76")

    # sunucu için
    app.run(debug=True, host='127.0.0.1', port=5050)

    # local my network
    # app.run(debug=True, host='192.168.1.76', port=5050)
