from model import db, Users, mailEvents
from fileFunctions import addimage, dosyasil
from flask import session, flash


def viewall():
    return Users.query.all()


def view(id):
    return Users.query.filter_by(id=id).first()


def viewstatu(statu):
    return Users.query.filter_by(statu=statu).all()


def add(name, surname, statu, gender, email, username, password, image=None):
    try:
        for row in viewall():
            if row.email == email:
                flash("Girilen E-posta kayıtlarımızda mevcut. Lütfen inceleyerek tekrar deneyiniz.", "warning")
                return False
            if row.username == username:
                flash("Girilen kullanıcı adı kayıtlarımızda mevcut. Lütfen inceleyerek tekrar deneyiniz.", "warning")
                return False
        if image:
            filename = useraddimage(image=image)
            newuser = Users(name=name, surname=surname, status=statu, imagePath=filename, gender=gender, email=email,
                            username=username, password=password)
        else:
            if gender == 'K':
                filename = "girl.png"
            else:
                filename = "boy.png"
            newuser = Users(name=name, surname=surname, status=statu, imagePath=filename, gender=gender, email=email,
                            username=username, password=password)
        db.session.add(newuser)
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Kullanıcı eklemede hata")
        print("Hata kodu:    ")
        print(str(e))
        flash("İşlem başarısız. Lütfen tekrar deneyiniz.", "warning")
        return False


def delete(id):
    try:
        deleteuser = view(id=id)
        mailEvents.sendmail(
            sendmailadress=deleteuser.email,
            subject="Kullanıcı Kaydınız Silinmiştir.",
            body=mailEvents.mailbody(kisi=deleteuser.name,
                                     icerik="Yapılan inceleme sonucunda kullanıcı hesabınız silinmiştir. Sağlıklı ve iyi günler dileriz.")
        )
        db.session.delete(deleteuser)
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Kullanıcı silmede hata alındı.")
        print("Hata: ")
        print(str(e))
        flash("İşlem başarısız. Lütfen tekrar deneyiniz.", "warning")
        return False


def nametoid(username):
    return Users.query.filter_by(username=username).first().id


def mysetting(id, name, surname, gender, email):
    data = view(id=id)
    try:
        data.name = name
        data.surname = surname
        data.gender = gender
        if data.email != email:
            data.email = email
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Ayarlar güncellemesinde hata alındı.")
        print("Ayarını değiştirmek isteyen kullanıcı adı: "+data.username)
        print("Hata Metni: "+str(e))
        return False


def useriamgeupdate(id, imagepath, oldimagepath):
    data = view(id=id)
    try:
        if imagepath.filename:
            dosyasil(filepath="img/user/", filename=oldimagepath)
            filepath = addimage(filepath="user", file=imagepath)
            data.imagePath = filepath
            db.session.commit()
            db.session.rollback()
            return True
    except Exception as e:
        print("Ayarlar resim güncellemesinde hata alındı.")
        print("Resmini değiştirmek isteyen kullanıcı adı: " + data.username)
        print("Hata Metni: " + str(e))
        return False


def useraddimage(image):
    try:
        if image.filename:
            filepath = addimage(filepath="user", file=image)
            return filepath
    except Exception as e:
        print("Ayarlar resim güncellemesinde hata alındı.")
        print("Resmini değiştirmek isteyen kullanıcı adı: " + session.get('username', ''))
        print("Hata Metni: " + str(e))
        return False


def accept(id):
    data = view(id=id)
    try:
        if data.useraccept:
            data.useraccept = False
            db.session.commit()
            db.session.rollback()
            result = mailEvents.sendmail(
                sendmailadress=data.email,
                subject="Kullanıcı Durumunuz Pasifleştirilmiştir.",
                body=mailEvents.mailbody(kisi=data.name, icerik="Yapılan incleme sonucunda kullanıcı hesabınız askıya alınmıştır. Hesabınız aktifleştiğinde size mail gönderilecektir.")
            )
        else:
            data.useraccept = True
            db.session.commit()
            db.session.rollback()
            result = mailEvents.sendmail(
                sendmailadress=data.email,
                subject="Kullanıcı Durumunuz Aktifleştirilmiştir.",
                body=mailEvents.mailbody(kisi=data.name, icerik="Yapılan incleme sonucunda kullanıcı hesabınız aktifleştirilmiştir. Hesabınızı aktif olarak kullanabilirsiniz.")
            )
        if result == 1:
            flash("Eposta bildirimi başarıyla gönderilmiştir.", "success")
        elif result == 2:
            flash("Gönderen ile alıcı epostası aynı olamaz.", "warning")
        else:
            flash("Eposta bildirimi gönderilirken hata alındı.", "warning")
        return True
    except Exception as e:
        print("Kullanıcı aktif/pasif kısmında hata alındı.")
        print("Resmini değiştirmek isteyen kullanıcı adı: " + session.get('username', ''))
        print("Hata Metni: " + str(e))
        return False


def updatepassword(userid, password):
    data = view(id=userid)
    try:
        data.password = password
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Şifre Değiştirme yapılırken hata alındı.")
        print("Hata metni:" + str(e))
        return False


def countusertype(statu):
    return Users.query.filter_by(statu=statu).all()


def update(id, name, surname, statu, gender, useremail, username):
    try:
        data = view(id=id)
        if not checkusernameandemail(id=id, email=useremail, username=username):
            return False
        data.name = name
        data.surname = surname
        data.statu = statu
        data.gender = gender
        data.email = useremail
        data.username = username
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Kullanıcı güncellenirken hata alındı.")
        print("Hata metni:" + str(e))
        flash("İşlem başarısız. Lütfen tekrar deneyiniz.", "warning")
        return False


def checkusernameandemail(email, username, id=None):
    if id:
        data = view(id=id)
        for row in viewall():
            if row.email == email and data.email != row.email:
                return False
            if row.username == username and data.username != row.username:
                flash("Girilen kullanıcı adı kayıtlarımızda mevcut. Lütfen inceleyerek tekrar deneyiniz.", "warning")
                return False
    else:
        for row in viewall():
            if row.email == email:
                return False
            if row.username == username:
                flash("Girilen kullanıcı adı kayıtlarımızda mevcut. Lütfen inceleyerek tekrar deneyiniz.", "warning")
                return False
    return True
