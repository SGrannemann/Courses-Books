# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)


@app.route('/')  # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "<h1>Hello!</h1>"


@app.route('/puppy_latin/<name>')  # Fill this in!
def puppylatin(name: str):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name.endswith('y'):
        return "<h1> {} </h1>".format(name[:-1] + 'iful')
    elif not name.endswith('y'):
        return "<h1> {} </h1>".format(name + 'y')


if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
