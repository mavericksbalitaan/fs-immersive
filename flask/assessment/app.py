from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/greeting/<name>")
def name(name):
    return render_template("index.html", name=name)


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        phone = request.form["phone"]
        street = request.form["street"]
        states = request.form["states"]
        zip = request.form["zip"]
        return render_template(
            "confirmation.html",
            fname=fname,
            lname=lname,
            phone=phone,
            street=street,
            states=states,
            zip=zip,
        )
    return redirect("/contact")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        session["is_loggedIn"] = True
        session["username"] = username
        session["password"] = password
        return redirect("/login")

    return render_template("login.html")


@app.route("/clear")
def clear():
    session.clear()
    return redirect("/login")


@app.route("/admin")
def admin():
    if session:
        if session["is_loggedIn"] == True:
            return render_template("admin.html")
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
