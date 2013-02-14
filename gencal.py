from pprint import pprint
from calendar import calendar
import datetime

translate_sundays = [1, 2, 3, 4, 5, 6, 0]
day_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def gen_calendar(start_date, end_date):
    prev_month_num = None

    all_months = {}
    this_month = []

    for single_date in daterange(start_date, end_date):
        this_month_num = single_date.month
        if prev_month_num != this_month_num:
            if this_month != []:
                all_months[prev_month_num] = this_month
                this_month = []
            prev_month_num = this_month_num

        this_month.append(single_date)

    if this_month != []:
        all_months[this_month_num] = this_month

    months_by_week = {}

    for month_num, month in all_months.items():
        all_weeks = []
        this_week = [None, None, None, None, None, None, None]
        for day in month:            
            weekday_num = (day.weekday() + 1) % 7
            if weekday_num == 0: # Sunday
                all_weeks.append(this_week)
                this_week = [None, None, None, None, None, None, None]
            weekday_name = day_names[weekday_num]
            day_num = day.day
            this_week[weekday_num] = day_num

        if this_week != [None, None, None, None, None, None, None]:
            all_weeks.append(this_week)

        months_by_week[month_num] = all_weeks

    return months_by_week

if __name__ == '__main__':
    start_date = datetime.datetime.now()
    end_date = start_date + datetime.timedelta(days=90)
    cal = gen_calendar(start_date, end_date)

    for month_num, month in cal.items():
        month_name = month_names[month_num - 1]
        print month_name
        pprint(month)
        print