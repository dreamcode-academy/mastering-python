from datetime import date, datetime, time, timedelta


def calculate_days_left(event_date):
    current_date = datetime.now()
    time_to_event = event_date - current_date
    return time_to_event.days

print(calculate_days_left(datetime(2024, 12, 25)))




'''
my_date = date(2023, 12, 25)
str_date = '2021-12-24'
format_date = datetime.strptime(str_date,'%Y-%m-%d')

#print(my_date.strftime('%Y/%m/%d'))

print(format_date.month)
'''
# time

my_time = time(14,30)
#print(my_time)

# date time

my_date_time = datetime.combine(date(2023,12,25), time(14,30))

#print(my_date_time)


