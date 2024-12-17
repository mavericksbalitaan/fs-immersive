from flask import Flask, redirect, render_template, request, session, url_for

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

        if (
            session["fname"]
            or session["lname"]
            or session["email"]
            or session["state"]
            or session["city"]
            or session["zipcode"]
        ):
            return render_template(
                "index.html",
                fname=session["fname"],
                lname=session["lname"],
                email=session["email"],
                state=session["state"],
                city=session["city"],
                zipcode=session["zipcode"],
            )
    else:
        if session:
            if (
                session["fname"]
                or session["lname"]
                or session["email"]
                or session["state"]
                or session["city"]
                or session["zipcode"]
            ):
                return render_template(
                    "index.html",
                    fname=session["fname"],
                    lname=session["lname"],
                    email=session["email"],
                    state=session["state"],
                    city=session["city"],
                    zipcode=session["zipcode"],
                )
        else:
            return render_template("index.html")


# test for session
@app.route("/session")
def sesh():
    if session:
        if (
            session["fname"]
            or session["lname"]
            or session["email"]
            or session["state"]
            or session["city"]
            or session["zipcode"]
        ):
            return f"Session: {session['fname']} {session['lname']} {session["email"]} {session['state']} {session['city']} {session['zipcode']}"
    else:
        return redirect("/")


# clear session
@app.route("/clear")
def clr():
    session.clear()
    return "Session cleared"


if __name__ == "__main__":
    app.run(debug=True, port=3000)
