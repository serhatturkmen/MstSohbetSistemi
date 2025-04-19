from model import Mail, db

from flask import render_template
import model.websettingEvents as websetting
from config import siteurl

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def view():
    return Mail.query.first()


def update(smtpserver, smtpemail, smtppassword, smtpport):
    try:
        updatemail = Mail.query.first()
        updatemail.smtpserver = smtpserver
        updatemail.smtpemail = smtpemail
        updatemail.smtppassword = smtppassword
        updatemail.smtpport = smtpport
        db.session.commit()
        db.session.rollback()
        return True
    except Exception as e:
        print("Mail güncellemede hata alındı.")
        print("Hata mesajı:: ")
        print(str(e))
        return False


def sendmail(sendmailadress, subject, body, inhtml=True):
    mailinformation = view()
    mailadress = mailinformation.smtpemail
    mailpass = mailinformation.smtppassword
    mailserver = mailinformation.smtpserver
    mailport = int(mailinformation.smtpport)
    if mailadress == sendmailadress:
        return 2
    message = MIMEMultipart()
    message["From"] = mailadress
    message["To"] = sendmailadress
    message["Subject"] = subject
    body = body
    if inhtml:
        body_text = MIMEText(body, "html")
    else:
        body_text = MIMEText(body, "plain")
    message.attach(body_text)

    try:
        mail = smtplib.SMTP(host=mailserver, port=mailport)
        mail.ehlo()
        mail.starttls()
        mail.login(mailadress, mailpass)
        mail.sendmail(message["From"], message["To"], message.as_string())
        result = 1
        mail.close()
    except Exception as e:
        print(e)
        sys.stderr.write("Bir hata oluştu. Tekrar deneyin...")
        result = 3
        sys.stderr.flush()
    return result


def mailbody(kisi, icerik):
    ayar = websetting.view()
    body = render_template('mailtemplate.html', ayar=ayar, kisi=kisi, icerik=icerik, siteurl=siteurl)
    return body
