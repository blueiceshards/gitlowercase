from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)

"""
@app.route('/ramen/<name>')
def view_ramen(name):
    return render_template('ramen.html', name=name, uppercase=name.upper(), spice=flavor_to_ingredients[name]['spice'], vegetarian=flavor_to_ingredients[name]['vegetarian'], msg_level=flavor_to_ingredients[name]['msg_level'])

flavor_to_ingredients = {
  'chicken': {
    'spice': 1,
    'vegetarian': 'No',
    'msg_level': 5
  },
  'seafood': {
    'spice': 10,
    'vegetarian': 'No',
    'msg_level': 5
  },
  'veggie': {
    'spice': 1,
    'vegetarian': 'Yes',
    'msg_level': 10
  },
}
"""

data = pd.read_csv('ramenrater.csv', engine='python')

@app.route('/ramen/<name>')
def view_ramen(name):
    return render_template('ramen.html', name=name, brand=info(name)[0], style=info(name)[1], country=info(name)[2], stars=info(name)[3])

def info(name):
  row = data.loc[data['Variety']==name].index[0]
  return (data['Brand'][row], data['Style'][row], data['Country'][row], data['Stars'][row])


""">>> data.loc[data['Variety']=='Pokemon Shoyu Ramen'].index[0]
1
>>> data.loc[data['Variety']=='Pokemon Shoyu Ramen'].index.values
array([   1, 1632])
>>> """