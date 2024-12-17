from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>INDEX</h1>"


@app.route("/display-name/<name>")
def displayName(name):
    return f"<h1>Display Name: {name.capitalize()}</h1>"


@app.route("/display-food/<food>")
def displayFood(food):
    return f"<h1>Favorite Food: {food.capitalize()}</h1>"


@app.route("/display-vacation/<vacation>")
def displayVacation(vacation):
    return f"<h1>Favorite Vacation Destination: {vacation.capitalize()}</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=3000)
