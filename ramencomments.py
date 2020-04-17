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

data.loc[data['Variety']=='Pokemon Shoyu Ramen'].index[0]
data.loc[data['Variety']=='Pokemon Shoyu Ramen'].index.values


"""