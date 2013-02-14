from flask import Flask, render_template
import datetime
from gencal import gen_calendar

app = Flask(__name__)

app.debug = True

start_date = datetime.datetime.now()
end_date = start_date + datetime.timedelta(days=90)
test_cal = gen_calendar(start_date, end_date)
english_month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

@app.route('/')
def home():
    return render_template('index.html', calendar=test_cal, month_names=english_month_names)

@app.route('/picker/')
def picker():
    return render_template('picker.html')

if __name__ == '__main__':
    app.run()