from flask import Flask, redirect, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["fname"] = request.form["fname"]
        session["lname"] = request.form["lname"]
        session["email"] = request.form["email"]
        session["state"] = request.form["state"]
        session["city"] = request.form["city"]
        session["zipcode"] = request.form["zipcode"]

        return render_template("index.html")
    return render_template("index.html")


# test for session
@app.route("/session")
def sesh():
    return render_template("index.html")


# clear session
@app.route("/clear")
def clr():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
