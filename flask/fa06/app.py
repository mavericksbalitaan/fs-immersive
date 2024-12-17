from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def index():
    if "count" in session:
        session["count"] += 1
        return render_template("index.html", count=session["count"])
    else:
        session["count"] = 0
        return render_template("index.html", count=session["count"])


# When you visit localhost:5000/addtwo the counter should increment by two.
@app.route("/addtwo")
def addtwo():
    session["count"] += 2
    return render_template("index.html", count=session["count"])


# When you visit localhost:5000/reset the counter should reset back to 0.
@app.route("/reset")
def clr():
    session["count"] = 0
    return render_template("index.html", count=session["count"])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
