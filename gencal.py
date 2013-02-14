from pprint import pprint
from calendar import calendar
import datetime

cal = calendar(6) # week starts on Sunday
translate_sundays = [1, 2, 3, 4, 5, 6, 0]
day_names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

if __name__ == '__main__':
    start_date = datetime.datetime.now()
    end_date = start_date + datetime.timedelta(days=25)

    prev_month_num = None

    all_months = []
    this_month = []

    for single_date in daterange(start_date, end_date):
        this_month_num = single_date.month
        if prev_month_num != this_month_num:
            print 'New month!'
            prev_month_num = this_month_num
            if this_month != []:
                print this_month
                all_months.append(this_month)
                this_month = []

        this_month.append(single_date)

    if this_month != []:
        all_months.append(this_month)

    pprint(all_months)

    for month in all_months:
        all_weeks = []
        this_week = [None, None, None, None, None, None, None]
        for day in month:            
            weekday_num = (day.weekday() + 1) % 7
            if weekday_num == 0: # Sunday
                all_weeks.append(this_week)
                this_week = [None, None, None, None, None, None, None]
            weekday_name = day_names[weekday_num]
            this_week[weekday_num] = day

        if this_week != [None, None, None, None, None, None, None]:
            all_weeks.append(this_week)

        pprint(all_weeks)