from flask import Blueprint, render_template, url_for, redirect, request, flash, session
from model.authEvents import logincontrol
from model import userEvents, websettingEvents
import random

auth = Blueprint('auth', __name__)

@auth.route("/register", methods=['GET', 'POST'])
@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form.get("event", "") == "login":            
            username = request.form.get('usernamelogin', '')
            sonuc = logincontrol(username=username, password=request.form.get('userpasslogin',  ''))
            print(sonuc)
            if sonuc == 1:
                session['name'] = username
                session['userid'] = userEvents.nametoid(username=username)
                session['login'] = True
                session['statu'] = "admin"
                session['room'] = None
                return redirect(url_for('admin.adminIndex'))
            elif sonuc == 2:
                session['name'] = username
                session['userid'] = userEvents.nametoid(username=username)
                session['login'] = True
                session['statu'] = "user"
                session['room'] = None
                return redirect(url_for('home.index'))
            elif sonuc == 4:
                session['login'] = False
                flash("Hesabınızın aktifleşmesi için yönetici onayı bekleniyor.", "warning")
                return redirect(request.url)
            else:
                session['login'] = False
                flash("Kullanıcı adı veya şifre yanlış.", "warning")
                return redirect(request.url)
        if request.form.get("event", "") == "registerform":
            username = request.form.get("username", "")
            email = request.form.get("email", "")
            result = userEvents.checkusernameandemail(username=username, email=email)
            if result:
                result2 = userEvents.add(
                    name=request.form.get("name", ""),
                    surname=request.form.get("surname", ""),
                    email=email,
                    username=username,
                    password=request.form.get("password", ""),
                    gender=request.form.get("gender", ""),
                    statu=2)
                if result2:
                    flash('İsteğiniz alınmıştır. Size en yakın zamanda geri dönüş sağlanacaktır.', 'success')
                    return redirect(request.url)
                else:
                    flash('İşlem sırasında hata alınmıştır. Bu hata kısa zamanda çözülecektir.', 'danger')
                    return redirect(request.url)
            else:
                flash('Girdiğiniz email veya kullanıcı adı kullanılmaktadır.', 'danger')
                return redirect(request.url)
    return render_template("login.html", setting=websettingEvents.view())


@auth.route("/forgotpassword", methods=['GET', 'POST'])
def forgotpassword():
    if request.method == "POST":
        if request.form.get("event", "") == "forgotpasswordform":
            pass
        return redirect(request.url)
    return render_template("forgotpass.html")


@auth.route("/logout", methods=['GET', 'POST'])
def logout():
    session['name'] = None
    session['userid'] = None
    session['login'] = False
    session['statu'] = None
    return redirect(url_for('auth.login'))


@auth.route('/kayitol', methods=['GET', 'POST'])
def kayitol():
    randSayi1 = random.randint(51, 99)
    randSayi2 = random.randint(10, 50)
    randislem = random.randint(1, 2)
    dogrulamaDizisi = dogrulama.derle(sayi1=randSayi1, sayi2=randSayi2, islem=randislem)
    dogrulamaMetni = dogrulamaDizisi[0]
    sonuc = dogrulamaDizisi[1]
    session['kod'] = sonuc
    print(sonuc)
    if request.method == 'POST':
        girilenSonuc = int(request.form['dogrulama'])
        print(girilenSonuc)
        if(girilenSonuc == session.get('kod','')):
            isim = request.form['name']
            soyad = request.form['surname']
            kuladi = request.form['username']
            eposta = request.form['email']
            parola = request.form['pass']
            bilgi = userEvents.kullanıcıEkle(kuladi, parola, isim, soyad, eposta)
            if bilgi == 1:
                flash("Kayıt işleminiz başarıyla tamamlanmıştır.", 'success')
            elif bilgi == 2:
                flash("Sistemde girdiğiniz e-posta adresiniz kayıtlıdır. Girdiğiniz e-posta adresiyle tekrardan kayıt yapılamaz.", 'warning')
            return render_template('status.mst')
        else:
            bilgi = "İşlem sonucunu yanlış girdiniz. Lütfen tekrar giriniz."
            return render_template('kayitol.mst', dogrulamaMetni=dogrulamaMetni, bilgi=bilgi)
    return render_template('kayitol.mst', dogrulamaMetni=dogrulamaMetni)
