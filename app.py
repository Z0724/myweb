from flask import render_template, redirect, request, url_for, flash
from web import create_app
from web.model import User

app = create_app('MysqlConfig')

@app.route('/')
def index():
    return render_template('n_index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    return render_template('/users/login.html')

@app.route('/reg',methods=['POST','GET'])
def reg():
    return render_template('/users/reg.html')

# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
	app.run(debug=True)
