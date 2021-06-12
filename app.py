#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Indecrypt 2.

Encrypt and decrypt data.
"""
import sys
import pickle
import webview
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
passwords = pickle.load(open("passwords.dat", "br"))


@app.route("/")
def index():
    """Page /."""
    return render_template("index.html")


@app.route("/home")
def home():
    """Home page."""
    if session.get("loggedin", "false") == "true":
        return render_template("home.html")
    return redirect("/login")


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Login page."""
    if request.method == 'POST':
        if request.form["username"] in passwords and request.form["password"] == passwords[request.form["username"]]:
            session["loggedin"] = "true"
            return redirect("/home")
        return render_template("bad_login.html")
    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    Logout page.
    
    :return: Redirection to /login
    :rtype: werkzeug.wrappers.response.Response
    """
    session["loggedin"] = "false"
    return redirect("/login")


@app.route("/favicon.ico")
def favicon():
    """Favicon."""
    return redirect("/static/favicon.ico")


@app.route("/dev")
def dev():
    """Page /dev."""
    return session


@app.route("/app/encrypt")
def app_encrypt():
    """
    Page /app/encrypt.
    Encrypt files.
    
    :return: DESCRIPTION
    :rtype: str
    """
    return render_template("app_encrypt.html")


if __name__ == "__main__":
    app.secret_key = b'\x86}0\xaan6\xa5K\xe8fF\x8a!h\xeaK\xbc\x8bWP\\\xc0\x18\x01'
    if "-h" in sys.argv or "--help" in sys.argv:
        print("Indecrypt 2 Server")
        print()
        print("Usage :")
        print("\tapp.py [-d | --debug | -p | --production] [-h | --help]")
        print()
        print("Description :")
        print("\tIndecrypt 2")
        print("\tEncrypt and decrypt files")
        print()
        print("Parameters :")
        print("\t-d, --debug : Start server in debug mode")
        print("\t-p, --production : start server in production mode")
        sys.exit(1)
    if "-d" in sys.argv or "--debug" in sys.argv:
        print("Starting in debug mode")
        app.run(host="localhost", port=8080, debug=True)
    elif "-p" in sys.argv or "--production" in sys.argv:
        print("Starting in production mode")
        app.run(host="localhost", port=80, debug=False)
    else:
        print("Starting in standard mode")
        webview.create_window("Indecrypt 2", app)
        webview.start(http_server=True)
