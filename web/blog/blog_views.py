from . import blog
from web.blog.form import RegForm, LoginForm
from web.model import User
from web.expand.other import mail, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required


@blog.route('/post')
def post():
    return render_template('blogpost.html')


@blog.route('/reg',methods=['POST','GET'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
        username=form.username.data, password=form.password.data)
        # add to db table
        db.session.add(user)
        db.session.commit()
        flash("註冊成功")
        return redirect(url_for('blog.login'))
    return render_template('/users/reg.html', form=form)

@blog.route('/login',methods=['POST','GET'])
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

@blog.route('/logout',methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    flash("您已經登出")
    return redirect(url_for('index'))
