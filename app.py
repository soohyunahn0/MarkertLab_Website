from flask import Flask, render_template
from people import curr_lab_people, former_lab_people
from publications import lab_publications

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/people")
def people():
    return render_template("people.html", curr_lab_people=curr_lab_people, former_lab_people=former_lab_people)

@app.route("/research")
def research():
    return render_template("research.html")

@app.route("/FRI")
def FRI():
    return render_template("FRI.html")

@app.route("/publications")
def publications():
    return render_template("publications.html", lab_publications=lab_publications)
