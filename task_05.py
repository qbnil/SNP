import datetime
import time

def data_in_future(days):
    if isinstance(days, (int)):
        tday = datetime.date.today()

        needed_data = tday + datetime.timedelta(days)

        return "{} {}".format(needed_data.strftime("%d-%m-%Y"), time.strftime("%H:%M:%S"))
    else:
        tday_default = datetime.date.today()
        return f"{tday_default.strftime('%d-%m-%Y')} {time.strftime('%H:%M:%S')}"

# print(data_in_future(None))
# print(data_in_future(3))