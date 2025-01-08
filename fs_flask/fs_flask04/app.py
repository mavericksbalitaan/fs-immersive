from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def displayUsers():
    users = User.query.all()
    return render_template("displayUsers.html", users = users)

@app.route("/users/new")
def newuser():
    return render_template("addUser.html")

@app.route("/users/create", methods=["POST"])
def createuser():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]

        newuser = User(fullname=firstname + " " + lastname, email=email)
        db.session.add(newuser)
        db.session.commit()
        return redirect("/users")

@app.route("/users/<int:id>/destroy")
def deleteuser(id):
    deleteduser = User.query.get(id)
    db.session.delete(deleteduser)
    db.session.commit()
    return redirect("/users")

# show user details
@app.route("/users/<int:id>", methods=["GET", "POST"])
def showuser(id):
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]

        updateuser = User.query.get(id)
        updateuser.fullname = firstname + " " + lastname
        updateuser.email = email
        db.session.commit()
        return redirect("/users")

    user = User.query.get(id)
    return render_template("showUser.html", user = user)

# edit user details
@app.route("/users/<int:id>/edit")
def edituser(id):
    user = User.query.get(id)
    return render_template("editUser.html", user = user)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.datetime.today())

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
