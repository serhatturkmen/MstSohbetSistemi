from flask import session, flash, redirect, url_for, Blueprint
from model import chatEvents
from flask_socketio import emit, join_room, leave_room
from dateFunctions import getdate
from emoji import emojize

from controller.homeController import home
from controller.authController import auth
from controller.adminController import admin

from app_instance import app, socketio

app.register_blueprint(admin)
app.register_blueprint(auth)
app.register_blueprint(home)

#app.register_error_handler(404, home.notfound)
#app.register_error_handler(405, home.notfounded)


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
        return redirect(url_for('auth.login'))


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
        return redirect(url_for('auth.login'))


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
        return redirect(url_for('auth.login'))


if __name__ == '__main__':
    # first use
    # socketio.run(app, port=5050, debug=True, host="192.168.1.76")

    # sunucu için
    # app.run(debug=True, host='127.0.0.1', port=5050)

    socketio.run(app, port=5050, debug=True, host="127.0.0.1")

    # local my network
    # app.run(debug=True, host='192.168.1.76', port=5050)
