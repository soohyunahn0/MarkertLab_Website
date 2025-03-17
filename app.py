from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "gUG*7BNmM*[*hUd7&y6hb}GlTcub`C"

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/people")
def people():
    return render_template("people.html")

@app.route("/research")
def research():
    return render_template("research.html")

@app.route("/FRI")
def FRI():
    return render_template("FRI.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")
