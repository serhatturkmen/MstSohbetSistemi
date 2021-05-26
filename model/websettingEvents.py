from model import WebSetting, db
from fileFunctions import addimage


def view():
    return WebSetting.query.first()


def update(title, metakeyword, metatitle, analitik, projectweek):
    try:
        data = view()
        data.title = title
        data.metakeyword = metakeyword
        data.metatitle = metatitle
        data.analitik = analitik
        data.projectweek = projectweek
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Site ayarlarında güncelleme yapılırken hata alındı.")
        print("Hata mesajı::")
        print(str(e))
        return False


def updateicon(ikon):
    try:
        updatewebsetting = view()
        filename = addimage("", ikon)
        updatewebsetting.ikon = filename
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Site ayarlarında ikon güncellemesi yapılırken hata alındı.")
        print("Hata mesajı::")
        print(str(e))
        return False

