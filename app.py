from flask import render_template, redirect, request, url_for, flash
from web import app

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('n_index.html')


if __name__ == "__main__":
	app.run(debug=True)
