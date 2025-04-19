from flask import Blueprint, session, flash, request, redirect, url_for, render_template
from model import websettingEvents, userEvents, authEvents

admin = Blueprint("admin", __name__)

@admin.route('/', methods=['GET', 'POST'])
def adminIndex():
    if authEvents.islogin(1):
        if request.method == "POST":
            if request.form.get("event", "") == "mailform":
                pass
        return render_template("admin/index.html",
                               setting=websettingEvents.view(),
                               user=userEvents.view(id=session.get("userid", "")))
    else:
        flash("Yetkisiz işlem.", "warning")
        return redirect(url_for("auth.login"))


@admin.route('/users/', methods=['GET', 'POST'])
def adminUsers():
    if request.method == "POST":
        if request.form.get("event", "") == "adduser":
            pass
        elif request.form.get("event", "") == "updateuser":
            pass
        elif request.form.get("event", "") == "deleteuser":
            pass
        elif request.form.get("event", "") == "acceptuser":
            pass
        elif request.form.get("event", "") == "disapprovaluser":
            pass
    return render_template("admin/user.html",
                           user=userEvents.view(session.get("userid", "")),
                           setting=websettingEvents.view(),
                           users=userEvents.viewall())


@admin.route('/banneduser/', methods=['GET', 'POST'])
def adminBannedUser():
    if session.get("login", ""):
        if session.get("statu", "") == "admin":
            if request.method == "POST":
                if request.form.get("event", "") == "mailform":
                    pass
            return "Admin banlanan kullanıcılar"
    else:
        return redirect(url_for("auth.login"))


@admin.route('/mailsetting', methods=['GET', 'POST'])
def adminMailSetting():
    if request.method == "POST":
        if request.form.get("event", "") == "mailform":
            pass
    return "Admin mail ayarları"


@admin.route('/mysetting', methods=['GET', 'POST'])
def mysetting():
    if request.method == "POST":
        if request.form.get("event", "") == "mailform":
            pass
    return render_template("admin/mysetting.html",
                           user=userEvents.view(session.get("userid", "")),
                           setting=websettingEvents.view(),
                           users=userEvents.viewall())

