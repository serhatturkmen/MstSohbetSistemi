from chat import siteurl
from model import token, mailEvents, userEvents, db
import uuid


def isthereview(tokenid):
    if token.query.filter_by(tokenid=tokenid).first():
        if token.query.filter_by(tokenid=tokenid).first().statu:
            return True
    else:
        return False


def tokenstatu(id):
    if token.query.filter_by(id=id).first().statu:
        return True
    else:
        return False


def tokenfalse(tokenid):
    falsetoken = token.query.filter_by(tokenid=tokenid).first()
    falsetoken.statu = False
    db.session.commit()
    db.session.rollback()


def addToken(process, userid, statu=True):
    unicid = str(uuid.uuid1())
    newToken = token(
        tokenid=unicid,
        process=process,
        statu=statu,
        userid=userid
    )
    db.session.add(newToken)
    db.session.commit()
    db.session.rollback()
    return unicid


def addforgotpass(kuladi, eposta, process):
    userid = userEvents.nametoid(kuladi)
    unicid = addToken(process=process, userid=userid)
    icerik = '''
        Şifre sıfırlama talebinde bulundunuz.Eğer siz değilseniz işlem yapmayınız. <br/>
        Sıfırlama talebinde bulunduysanız linke tıklayınız.
        <a target="_blank" href="'''+siteurl+'''/token/'''+unicid+'''">Yeni Şifre belirle</a>
    '''
    body = mailEvents.mailbody(kisi=kuladi, icerik=icerik)
    result = mailEvents.sendmail(sendmailadress=eposta, subject='Şifre sıfırlama', body=body)
    print(kuladi+' şifre sıfırlama talebinde bulundu. Eposta '+eposta+' adresine gönderildi. Token oluşturuldu.')
    return result


def tokenuserid(tokenid):
    return token.query.filter_by(tokenid=tokenid).first().userid
