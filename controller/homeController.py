# -*- coding: utf-8 -*-
from flask import Blueprint, session, redirect, url_for, render_template, request, flash
from model import websettingEvents, authEvents, userEvents, chatEvents
from app_instance import socketio
from emoji import emojize


home = Blueprint("home", __name__)


@home.route('/chat', methods=['GET', 'POST'])
def chat():
    if authEvents.islogin(2) or authEvents.islogin(1):
        session["chatid"] = None
        if request.method == "POST":
            if request.form.get("event", "") == "addchatsubmit":
                username = request.form.get("username", "")
                if userEvents.nametoid(username=username):
                    if chatEvents.viewbyusersid(user1=session.get("userid", ""),
                                                user2=userEvents.nametoid(username=username)):
                        flash(
                            "Girilen kullanıcı adı ile bir sohbetiniz zaten var. Lütfen kontrol ederek tekrar deneyiniz.",
                            "warning")
                        return redirect(request.url)
                    chatEvents.add(user1=session.get("userid", ""), user2=userEvents.nametoid(username=username))
                    return redirect(request.url)
                else:
                    flash("Girilen kullanıcı adı bulunmamaktadır. Lütfen kontrol ederek tekrar deneyiniz.", "danger")
                    return redirect(request.url)
        chatting_users = chatEvents.chattinguser(userid=int(session.get("userid", "")))
        return render_template('chattemplate.html',
                               chatting=False,
                               chatting_users=chatting_users,
                               users=userEvents.view)
    else:
        return redirect(url_for('auth.login'))


@home.route('/chat/<string:chatid>', methods=['GET', 'POST'])
def chatwithid(chatid):
    if authEvents.islogin(2) or authEvents.islogin(1):
        if request.method == "POST":
            if request.form.get("event", "") == "addchatsubmit":
                username = request.form.get("username", "")
                if userEvents.nametoid(username=username):
                    if chatEvents.viewbyusersid(user1=session.get("userid", ""), user2=userEvents.nametoid(username=username)):
                        flash("Girilen kullanıcı adı ile bir sohbetiniz zaten var. Lütfen kontrol ederek tekrar deneyiniz.",
                              "warning")
                        return redirect(request.url)
                    chatEvents.add(user1=session.get("userid", ""), user2=userEvents.nametoid(username=username))
                    return redirect(request.url)
                else:
                    flash("Girilen kullanıcı adı bulunmamaktadır. Lütfen kontrol ederek tekrar deneyiniz.", "danger")
                    return redirect(request.url)
        if chatEvents.controlchatid(userid=session.get("userid", ""), chatid=chatid):
            session["chatid"] = chatid
            chatting_users = chatEvents.chattinguser(userid=int(session.get("userid", "")))
            messages = chatEvents.getmessages(chatid)
            messaginguser = chatEvents.getmaessaginguser(chatid=chatid, userid=session.get("userid", ""))
            return render_template('chattemplate.html',
                                   async_mode=socketio.async_mode,
                                   chatting=True,
                                   messages=messages,
                                   chatting_users=chatting_users,
                                   users=userEvents.view,
                                   messaginguser=messaginguser,
                                   emojize=emojize)
        else:
            return redirect(url_for('.chat'))
    else:
        return redirect(url_for('auth.login'))


@home.route('/')
def index():
    if session.get("login", ""):
        print("Giriş yapılmış. Ona göre sayfa hazırla")
    else:
        return redirect(url_for(".login"))
    return render_template('index.html',
                           setting=websettingEvents.view(),
                           user=userEvents.view(id=session.get('userid', '')))


@home.errorhandler(404)
def notfound(error):
    print(error)
    return "not found 404"


@home.errorhandler(405)
def notfounded(error):
    print(error)
    return "not founded 405"
