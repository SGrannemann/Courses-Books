from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    name = "Jose"
    letters = list(name)
    puppies = ['Spike', 'Rufus', 'Sammy']
    pup_dictionary = {"pup_name": 'Sammy'}
    return render_template('home.html', name=name, letters=letters, puppies=puppies,  pup_dictionary=pup_dictionary)


@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)


@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')


@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('thankyou.html', first=first, last=last)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
