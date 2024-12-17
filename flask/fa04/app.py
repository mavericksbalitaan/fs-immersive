from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        state = request.form["state"]
        city = request.form["city"]
        zipcode = request.form["zipcode"]

        return render_template(
            "index.html",
            fname=fname,
            lname=lname,
            email=email,
            state=state,
            city=city,
            zipcode=zipcode,
        )
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
