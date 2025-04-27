from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///appointments.db"
db = SQLAlchemy(app)


@app.route("/")
def index():
    appointments = Appointment.query.all()
    return render_template("index.html", appointments=appointments)


@app.route("/new_appointment", methods=["GET", "POST"])
def new_appointment():
    if request.method == "POST":
        appointment_date = request.form["appointment_date"]
        appointment_time = request.form["appointment_time"]
        patient_name = request.form["patient_name"]
        complain = request.form["complain"]

        print(type(appointment_date))
        print(type(appointment_time))

        # change str to date and time object
        date = datetime.strptime(
            appointment_date, '%Y-%m-%d').date()
        time = datetime.strptime(
            appointment_time, '%H:%M').time()

        print(type(date))
        print(type(time))

        new_appointment = Appointment(appointment_date=date,
                                      appointment_time=time, patient_name=patient_name, complain=complain)
        db.session.add(new_appointment)
        db.session.commit()
        return redirect("/")

    return render_template("form.html")


@app.route("/cancel/<int:id>")
def cancel_appointment(id):
    cancel_appointment = Appointment.query.get(id)
    db.session.delete(cancel_appointment)
    db.session.commit()
    return redirect("/")


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    patient_name = db.Column(db.String(200), nullable=False)
    complain = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Appointment ${self.patient_name}>'


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
