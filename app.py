from flask import render_template, redirect, request, url_for, flash
from web import create_app
from web.model import User, IndexMessageBoard
from web.form import  IndexMessageForm
from web.blog.form import ArticleForm
from flask_mail import Mail, Message
from web.expand.other import mail, db
from sqlalchemy import desc

app = create_app('MysqlConfig')

@app.route('/')
def index():
    mb_message=db.session.query(IndexMessageBoard).order_by(desc(IndexMessageBoard.mb_id)).limit(5).all()
    return render_template('n_index.html',mb_message=mb_message)

@app.route('/')
def post():
    return render_template('blogpost.html')

@app.route('/Article',methods=['POST','GET'])
def Articless():
    form = ArticleForm()
    if form.validate_on_submit():
        from web.blog.model import Article
        Articles = Article(title=form.title.data,
                              content=form.content.data)
        # add to db table
        db.session.add(Articles)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('/blog/post.html', form=form)

@app.route('/test111',methods=['POST','GET'])
def test111():
    form = IndexMessageForm()
    if form.validate_on_submit():
        Message = IndexMessageBoard(mb_message=form.mb_message.data)
        # add to db table
        db.session.add(Message)
        db.session.commit()
        flash("碎念成功")
        return redirect(url_for('index'))
    return render_template('/users/test.html', form=form)

@app.route("/mail")
def sent_mail():
    msg = Message('測試', sender = app.config.get('MAIL_USERNAME'), recipients = ['asd123698745tw@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
	app.run(debug=True)
