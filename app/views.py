from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {"nickname": "LMN"}
    posts = [
        {"author":{"nickname":"zhangsan"},
         "body":"What a day it is"},
        {"author":{"nickname":"lisi"},
         "body":"hahahah"}
    ]
    return render_template("index.html", 
                            title = "Home", 
                            user = user,
                            posts = posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm() # 写成LoginForm很难找到出错地
    if form.validate_on_submit():
        # 在base.html模板中加入显示flash调试消息的功能，否则不显示
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template("login.html", 
                            title = "Sign in", 
                            form = form,
                            providers = app.config['OPENID_PROVIDERS'])

