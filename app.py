from flask import render_template, redirect, request, url_for, flash, abort
from web import create_app
from web.model import IndexMessageBoard
from web.form import  IndexMessageForm
from flask_mail import Mail, Message
from web.expand.other import mail, db
from sqlalchemy import desc


app = create_app('MysqlConfig')

@app.route('/')
def index():
    from web.blog.model import Article
    latest_articles = Article.query.order_by(Article.created_at.desc()).limit(5).all()
    mb_message=db.session.query(IndexMessageBoard).order_by(desc(IndexMessageBoard.mb_id)).limit(5).all()
    return render_template('n_index.html',mb_message=mb_message,latest_articles=latest_articles)

@app.route('/23')
def post():
    return render_template('blogpost.html')


@app.route('/soliloquize',methods=['POST','GET'])
def soliloquize():
    form = IndexMessageForm()
    if form.validate_on_submit():
        Message = IndexMessageBoard(mb_message=form.mb_message.data)
        # add to db table
        db.session.add(Message)
        db.session.commit()
        flash("碎念成功")
        return redirect(url_for('index'))
    return render_template('/users/soliloquize.html', form=form)

@app.route('/soliloquize/list')
@app.route('/soliloquize/list/<int:page>')
def soliloquize_list(page=1):
    from web.model import IndexMessageBoard
    soliloquize_list = IndexMessageBoard.query.order_by(IndexMessageBoard.mb_data.desc()).paginate(page=page, per_page=10)
    return render_template('/users/soliloquize_list.html',soliloquize_list=soliloquize_list)


@app.route("/mail")
def sent_mail():
    msg = Message('測試', sender = app.config.get('MAIL_USERNAME'), recipients = ['asd123698745tw@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


from web.admin import admin_model
with app.app_context():
    db.create_all()

if __name__ == "__main__":
	app.run(debug=True)
