from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Hello World!"

# Route for user sign up


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect("/login")

    return render_template("userSignup.html")

# Route for user log in


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session["loggedin"] = True
            session["userid"] = user.id
            return redirect("/posts")

        return redirect("/login")

    return render_template("userLogin.html")

# Route for displaying posts of the users


@app.route("/posts")
def posts():
    if session:
        if session["loggedin"] is True:
            posts = Post.query.filter_by(user_id=session["userid"]).all()
            return render_template("userPosts.html", posts=posts)
    return redirect("/login")

# Route for creating a new post


@app.route("/posts/create", methods=["GET", "POST"])
def createPost():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        post = Post(title=title, content=content, user_id=session["userid"])
        db.session.add(post)
        db.session.commit()

        return redirect("/posts")

    return render_template("formPost.html")


# Route for clearing sessions
@app.route("/logout")
def logoutUser():
    session.clear()
    return redirect("/login")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    posts = db.relationship("Post", backref="user")

    def __repr__(self):
        return f"<User {self.email}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Post '{self.content[:20]}...'>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
