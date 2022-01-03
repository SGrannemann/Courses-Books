# set up local environment for testing purposes
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
############################
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(
    client_id='599524362151-el55a53a77vfp0eo823k8f101ke0c7hm.apps.googleusercontent.com', client_secret='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', offline=True, scope=['profile', 'email'])
app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    # RETURN INTERNAL SERVER ERROR IF NOT LOGGED IN!
    # not something to do in production, just for demonstration
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)


@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html', email=email)


if __name__ == "__main__":
    app.run()
