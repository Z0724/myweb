from flask import render_template, redirect, request, url_for, flash
from web import create_app
from web.model import User, IndexMessageBoard
from web.form import RegForm, LoginForm, IndexMessageForm
from flask_mail import Mail, Message
from web.expand.other import mail, db
from flask_login import login_user, logout_user, login_required
from sqlalchemy import desc

app = create_app('MysqlConfig')

@app.route('/')
def index():
    mb_message=db.session.query(IndexMessageBoard).order_by(desc(IndexMessageBoard.mb_id)).limit(5).all()
    return render_template('n_index.html',mb_message=mb_message)

@app.route('/post')
def post():
    return render_template('blogpost.html')

@app.route('/test',methods=['POST','GET'])
def test():
    form = IndexMessageForm()
    if form.validate_on_submit():
        Message = IndexMessageBoard(mb_message=form.mb_message.data)
        # add to db table
        db.session.add(Message)
        db.session.commit()
        flash("碎念成功")
        return redirect(url_for('index'))
    return render_template('/users/test.html', form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            # 第二個參數是記得我的參數
            login_user(user, form.remember_me.data)
            flash("您已經成功的登入系統")
            # 利用request來取得參數next，上個頁面在哪
            next = request.args.get('next')
            # 自定義一個驗證的function來確認使用者是否確實有該url的權限
            # 另一個用法if not next_is_valid(next):
            # next_is_valid需要另外寫函式next_is_valid(url):return True
            if  next == None or not next[0]=='/':
                next = url_for('index')
            return redirect(next)
        else:
            #  如果資料庫無此帳號或密碼錯誤，就顯示錯誤訊息。
            flash('信箱或密碼錯誤')
    return render_template('/users/login.html',form=form)

@app.route('/logout',methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    flash("您已經登出")
    return redirect(url_for('test'))

@app.route('/reg',methods=['POST','GET'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
        username=form.username.data, password=form.password.data)
        # add to db table
        db.session.add(user)
        db.session.commit()
        flash("註冊成功")
        return redirect(url_for('login'))
    return render_template('/users/reg.html', form=form)

@app.route("/mail")
def sent_mail():
    msg = Message('測試', sender = app.config.get('MAIL_USERNAME'), recipients = ['asd123698745tw@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
	app.run(debug=True)
