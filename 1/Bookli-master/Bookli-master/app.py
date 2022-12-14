from functools import wraps

from flask import Flask, session, flash, redirect
from api.views import api
from frontend.views import website
from auth import auth

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"


app.secret_key = "pythonistrandomseceret@key"
app.register_blueprint(auth, url_prefix='/user')
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(website)


if __name__ == '__main__':
    app.run(debug=True)
