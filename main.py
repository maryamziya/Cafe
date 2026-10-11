from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = URLField('Cafe Location', validators=[DataRequired()])
    open_time = StringField('Opening Time (ex: 11AM or 3:30PM)', validators=[DataRequired()])
    close_time = StringField('Closing Time (ex: 11AM or 3:30PM)', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',  choices=['☕', '☕☕', '☕☕☕','☕☕☕☕','☕☕☕☕☕'] ,validators=[DataRequired()])
    wifi_strength = SelectField('Wifi Strength',choices=['✘','💪', '💪💪', '💪💪💪','💪💪💪💪','💪💪💪💪💪'], validators=[DataRequired()])
    power_socket_ability = SelectField('Power Socket Ability',choices=['✘','🔌', '🔌🔌', '🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        cafe_loc = form.cafe_location.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee = form.coffee_rating.data
        wifi = form.wifi_strength.data
        power = form.power_socket_ability.data
        new_row = [cafe_name,cafe_loc,open_time,close_time,coffee,wifi,power]
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
        redirect(url_for('cafes'))
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)




if __name__ == '__main__':
    app.run(debug=True)
