from flask import render_template, redirect, request, url_for, flash
from web import app, db
from web.model import User


@app.route('/',methods=['POST','GET'])
def index():
    return render_template('n_index.html')

# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
	app.run(debug=True)
