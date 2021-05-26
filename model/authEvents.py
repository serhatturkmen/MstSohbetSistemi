from model import db, Users, userEvents
from flask import session
from dateFunctions import getdate


def islogin(statu):
    user = userEvents.view(id=session.get("userid", ""))
    if user and session.get("login", ""):
        if user.status == statu:
            return True
    else:
        return False


def logincontrol(username, password):
    islogin = Users.query.filter_by(username=username, password=password).first()
    if islogin:
        if islogin.userAccept:
            if islogin.status == 1:
                lastseenupdate(islogin.id)
                return 1
            elif islogin.status == 2:
                lastseenupdate(islogin.id)
                return 2
            else:
                return 3
        else:
            return 4
    else:
        return False


def lastseenupdate(id):
    userdetail = userEvents.view(id=id)
    userdetail.lastSeenDate = getdate()
    db.session.commit()
    db.session.rollback()
    return True


def viewnamesurname(username):
    data = userEvents.view(userEvents.nametoid(username=username))
    return data.name + ' ' + data.surname


def isthereuser(username, email):
    data = Users.query.filter_by(username=username, email=email).first()
    if data:
        return True
    else:
        return False
