from web import app

app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql://root:12345@localhost/test"
app.config['SECRET_KEY']= 'ffsdfsddsbr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False