from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/about")
def about():
    return render_template("about_page.html")