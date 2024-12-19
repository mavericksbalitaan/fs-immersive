from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form["password"]
        confirmpassword = request.form["confirmpassword"]

        if password == confirmpassword:
            new_user = User(
                fname=request.form["fname"],
                lname=request.form["lname"],
                username=request.form["username"],
                password=request.form["password"],
                confirmpassword=request.form["confirmpassword"],
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect("/users")

        return render_template("index.html")

    return render_template("index.html")


@app.route("/users")
def usersList():
    users = User.query.all()
    return render_template("list.html", users=users)


class User(db.Model):
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    confirmpassword = db.Column(db.String(50), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
