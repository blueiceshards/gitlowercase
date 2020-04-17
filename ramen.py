from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('ramenrater.csv', engine='python')

L = []
for x in data['Variety']:
  L.append('/ramen/'+x)

@app.route('/ramen/<name>')
def view_ramen(name):
    return render_template('ramen.html', name=name, brand=info(name)[0], style=info(name)[1], country=info(name)[2], stars=info(name)[3])

def info(name):
  row = data.loc[data['Variety']==name].index[0]
  return (data['Brand'][row], data['Style'][row], data['Country'][row], data['Stars'][row])

@app.route('/')
def home():
    return render_template('home.html', urls=L)



