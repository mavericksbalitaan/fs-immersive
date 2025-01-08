from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime
import pytz

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.db"
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]

        newCourse = Course(name = name, description = description)
        db.session.add(newCourse)
        db.session.commit()

        courses = Course.query.all()

        return render_template("index.html", courses=courses)

    courses = Course.query.all()
    return render_template("index.html", courses=courses)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.datetime.now)

# must put these methods outside the template_filter
def suffix(d):
    return {1:'st',2:'nd',3:'rd'}.get(d%20,'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

@app.template_filter('format_utc_to_local')
def format_utc_to_local(value):
    if value is None:
        return ""
    # Convert UTC datetime to local time (e.g., US Eastern Time)
    utc_time = pytz.utc.localize(value)  # Ensure UTC is set if not present
    local_time = utc_time.astimezone(pytz.timezone('US/Eastern'))  # You can change this to any timezone
    # Format the datetime to the desired format
    changeToSuffix = local_time.strftime('%b %d %Y %I:%M%p')  # Example: "Dec 31 2024 12:30 PM"
    return custom_strftime('%b {S} %Y %I:%M%p', local_time)

@app.route("/deleteCourse/<int:id>")
def deleteCourse(id):
    course = Course.query.get(id)
    return render_template("deleteCourse.html", course=course)

@app.route("/courses/destroy/<int:id>")
def destroyCourse(id):
    if id:
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()

    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # current_date = datetime.datetime.now()
        # newCourse = Course(name = "Sample Course Name", description = "Sample Course Description", date_added = current_date)
        # db.session.add(newCourse)
        # try:
        #     db.session.commit()
        # except Exception as e:
        #     db.session.rollback()
        print(Course.query.all())
        app.run(debug=True)
