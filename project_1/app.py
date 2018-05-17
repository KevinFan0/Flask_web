from flask import Flask,request,render_template
from flask import current_app
from flask import make_response


app=Flask(__name__)
app_ctx=app.app_context() #程序上下文
app_ctx.push()


# @app.route('/')
# def index():
#     user_agent=request.headers.get('User-Agent')
#     return '<p>Your browser is %s</p>' %user_agent

@app.route('/')
def index():
    respons=make_response('<h1>This document carries a cookie!</h1>')
    respons.set_cookie('answer','42')
    return respons

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)