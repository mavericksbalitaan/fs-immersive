from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get("https://api.restful-api.dev/objects/7")
    data = r.json()
    return render_template("index.html", content = data)

if __name__ == "__main__":
    app.run(debug=True)
