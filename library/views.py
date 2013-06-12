from flask import render_template
from library import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')