from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/ramen/<name>')
def view_ramen(name):
    return render_template('ramen.html', name=name)