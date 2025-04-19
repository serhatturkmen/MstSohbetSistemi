import os
import uuid
from app_instance import app


def acceptfileextention(filename):
    izinliResimFormatlari = {'png', 'jpg', 'jpeg', 'gif', 'ico'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in izinliResimFormatlari


def dosyasil(filepath, filename):
    try:
        if filename != 'boy.png' or filename != 'girl.png':
            os.remove(os.path.join(app.root_path, 'static', filepath, filename))
    except:
        pass


def addimage(filepath, file):
    if file.filename == '':
        return False
    if file and acceptfileextention(file.filename):
        filename = str(uuid.uuid1()) + '.' + file.filename.rsplit('.', 1)[1].lower()
        file.save(os.path.join(app.root_path, 'static', 'img', filepath, filename))
        return filename
    else:
        return False


def iconEkle(file):
    if file.filename == '':
        return False
    if file and file.filename.rsplit('.', 1)[1].lower() in 'ico':
        dosyasil('img', 'favicon.ico')
        filename = str('favicon.' + file.filename.rsplit('.', 1)[1].lower())
        file.save(os.path.join(app.root_path, 'static', 'img', filename))
        return filename
    else:
        return False
