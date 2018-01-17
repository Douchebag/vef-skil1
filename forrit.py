from bottle import route, run
import os

@route("/")
def index():
    return "<a href='/about'>About</a> <a href='/biography'>Biography</a> <a href='/pictures'>Pictures</a>"
@route("/about")
def about():
    return "<h1>about</h1>"

@route("/biography")
def about():
    return "<h1>biography</h1>"

@route("/pictures")
def about():
    return "<h1>pictures</h1>"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))