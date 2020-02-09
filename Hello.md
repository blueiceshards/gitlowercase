Hello Golem!

We previous made the a static html page. It's like a word doc, where the contents of the page are always the same. Under that model, if we wanted to have page for 5 types of ramen, we would need to type out five of those pages. If we wanted to fix a typo in all of them, we would have to change each of the 5 files individually.

This time, we are going to make a dynamic web page. We will write one template, and that template will render the value of variables that we give it. The page will be dynamically generated, in that the page returned will be different depending on the url the user types.

For this dynamic generation, we are going to use a python webserver known as flask https://flask.palletsprojects.com/en/1.1.x/.

## Installation

First, we are going to install flask. You could install it globally on your computer, like you might install a normal program. But we could imagine a world in which you have different projects on your computer, that need different versions of flask.

So, we are going to create a sandbox for this gitlowercase project, that all the packages you need will be installed in.

First, check if you have the command `conda` already installed. If not, install miniconda for python 3 https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html.

Then, create a conda environment (the sandbox) for this project
`conda create --name ramen python=3.7`

Activate the environment
`source activate ramen`
Whenever you want to run the app in a new terminal session, you first need to run this to activate the conda environment.

Type `pip --version`, and you should see that it says (python 3.7).

Finally, install flask
`pip install Flask`
When you type `flask`, you should see the command information.

## Running the web app
I'm going to tell you the commands to run, so you can play with the web page and see that it works. Then I will go backwards and talk about how it works.

To start the app, run
`export FLASK_APP=ramen.py && flask run`
If, in the future, here it says that flask not found, check if you have run `source activate ramen` yet.

Then in a browser, go to http://127.0.0.1:5000/ramen/hi

You should see that as you change the 'hi' to different things, e.g. http://127.0.0.1:5000/ramen/blah, the word shows up on the web page.

We now have a dynamic web page! It shows different content depending on the url that you put in.

## How it works
There are two files to all this, `ramen.py`, and `templates/ramen.html`.

In `ramen.py`, there is one function, `def view_ramen`. It is decorated with `@app.route('/ramen/<name>')`. The `@app.route` specifies the url to match, specifically to match /ramen/<anything here>. It means that when you find a url matching this, show the stuff in the function.

And so what does the stuff in the function say? It only has one line, which is to return `render_template('ramen.html', name=name)`. That has two parts.
One, the `ramen.html` says to use the html file in `templates/ramen.html`.
The other, is `name=name`.

What's up with `name`? In this code block, we can see that `name` appears in three places. 1) the route url `/ramen/<name>`, 2) as an argument to our function `view_ramen(name)`, and as an argument passed to render_template `render_template('ramen.html', name=name)`.
```
@app.route('/ramen/<name>')
def view_ramen(name):
    return render_template('ramen.html', name=name)
```

By specifying `<name>` in the url, we are saying that whatever occurs after `/ramen/` should be saved as a variable called `name`.

Since we expect this variable coming from the url, the `view_ramen` function takes in this variable called `name`.

And finally, we want to pass this variable `name`, and whatever it's value is, to the template `ramen.html`.

If we open `ramen.html`, we can see a `{{ name }}`. This says to put the value of the variable called name, at the spot.

There is nothing magic about the word `name`. It's just a variable, you could call it `pokeball` for all that matters. It just needs to be consistent.

## Read up

This is all based off of the quickstart application in the flask documentation https://flask.palletsprojects.com/en/1.1.x/quickstart/. Please read these sections, in the following order:
- A minimal application
- Rendering templates
- Routing

## Homework

I set up a very simple thing that just puts the text in the url into a div. But this is not a ramen page.

### 1) play with the existing set up, so you are familiar with how it works.
Try adding a second variable to the render_template, that is a transformation of the one that comes in by url. E.g., the sentence should say "My ramen is hello. In all uppercase, this is HELLO".

### 2) use that url input to select some data, and show that data
E.g. define a dictionary that says
```
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
```

Then depending on whether the user types /ramen/chicken, /ramen/seafood, or /ramen/veggie, show the three pieces of information on the page

### 3) get data from your csv
Put your ramen data csv in this repository.

Install pandas. Make sure you have activated your ramen conda environment first!
`conda install pandas`

You can import pandas in your python file `import pandas as pd`, and read your csv in as a dataframe. When the user types /ramen/<name of ramen>, they should see a page with information from the csv for this ramen.
- After you read in the csv to a pandas df, use the ramen name to select the row. Then pass the row information into the render_template function, as you have previously done
- The page doesn't need to be pretty, focus on data slicing first
- Assume that the user will correctly type the name of the ramen, and don't worry when the page errors if there is a typo

## Extra credit

Make a home page that lists all possible ramen pages.

This `view_ramen` function is called an endpoint.
```
@app.route('/ramen/<name>')
def view_ramen(name):
```

You can easily make another endpoint by defining another function. Make a `home` function that matches the `/` url. Create a home page html file that it should render, and render it.

The `home` function should read the csv, get a list of all the ramen, and template it in the html file. For that, you will need to write a for loop in the template.

The `{{ name }}` syntax is based on a library called jinja, which flask uses to template their html. It also has for loops, which work like `{% for ramen in ramens %}`. This is their documentation https://jinja.palletsprojects.com/en/2.11.x/templates/. There is a lot we don't need that can get confusing, so please just read
- Synposis
- List of control structures (https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-control-structures), just the first two code blocks
- Variables (https://jinja.palletsprojects.com/en/2.11.x/templates/#variables)
