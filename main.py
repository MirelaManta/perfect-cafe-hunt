from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from dotenv import load_dotenv
import csv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
Bootstrap(app)

CSV_FILE = "cafe-data.csv"


def emoji_rating(elem, missing=""):
    rating_choice = []
    for i in range(0, 6):
        if missing != "" and i == 0:
            rating_choice += [missing]
        else:
            rating = ""
            for j in range(i):
                rating += elem
            rating_choice += [rating]

    return rating_choice


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location_url = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open_time = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close_time = StringField("Closing Time e.g 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", validators=[DataRequired()], choices=["☕️", "☕️☕️", "☕️☕️☕️",  "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"])
    wifi_rating = SelectField("Wifi Strength Rating", validators=[DataRequired()], choices=emoji_rating(elem="💪", missing="✘"))
    power_availability = SelectField("Power Socket Availability", validators=[DataRequired()], choices=emoji_rating(elem="🔌", missing="✘"))
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(CSV_FILE, "a", encoding="utf-8") as data_file:
            new_data = [form.cafe.data, form.location_url.data, form.open_time.data, form.close_time.data,
                        form.coffee_rating.data, form.wifi_rating.data, form.power_availability.data]
            writer = csv.writer(data_file)
            writer.writerow(new_data)

        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(CSV_FILE, newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
