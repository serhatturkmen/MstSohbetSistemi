from model import db, Chat, Message
from sqlalchemy import or_
from emoji import emojize


def viewall(): return Chat.query.all()


def view(id): return Chat.query.get(id)


def viewbyuserid(userid): return Chat.query.filter(or_(Chat.user1 == userid, Chat.user2 == userid)).all()


def controlchatid(userid, chatid):
    for chatids in viewbyuserid(userid):
        if int(chatid) == chatids.id:
            return True
    return False


def viewbyusersid(user1, user2):
    if Chat.query.filter_by(user1=user1, user2=user2).first():
        return True
    else:
        return False


def getmaessaginguser(chatid, userid):
    chatting = view(id=chatid)
    if chatting.user1 == userid:
        return chatting.user2
    else:
        return chatting.user1


def add(user1, user2):
    try:
        db.session.add(Chat(user1=user1, user2=user2))
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Chat oluşturmada hata alındı.")
        print("Hata:::")
        print(str(e))
        return False


def getmessages(chatid):
    return convertemoji(Message.query.filter_by(roomId=chatid).all())


def addmessage(roomid, userid, messagecontent, messagedate):
    try:
        newmessage = Message(
            roomId=roomid,
            userId=userid,
            messageContent=messagecontent,
            messageDate=messagedate
        )
        db.session.add(newmessage)
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Mesaj eklemede hata alındı.")
        print("Veriler")
        print("Roomid:", roomid)
        print("Userid:", userid)
        print("messagecontent:", messagecontent)
        print("messagedate:", messagedate)
        print("Hata Mesajı:::")
        print(str(e))
        return False


def chattinguser(userid):
    chats = []
    for chatted in viewbyuserid(userid=userid):
        if chatted.user1 == userid:
            chats.append({"userid": chatted.user2, "chatid": chatted.id})
        else:
            chats.append({"userid": chatted.user1, "chatid": chatted.id})
    return chats



def convertemoji(datas):
    for data in datas:
        data.messageContent = emojize(data.messageContent)
    return datas

