from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/third")
def third():
    return render_template("third.html")
    
@app.route("/fourth")
def fourth():
    return render_template("fourth.html")

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":

        if not request.form.get("Firstname") or not request.form.get("Lastname"):
            return("error")
        else:
            return render_template("answer.html", firstname=request.form.get("Firstname"), lastname=request.form.get("Lastname"))
    else:
        return render_template("hello.html")