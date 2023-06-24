import datetime
import time

def data_in_future(days):

    tday = datetime.date.today()

    needed_data = tday + datetime.timedelta(days)

    return "{} {}".format(needed_data.strftime("%d-%m-%Y"), time.strftime("%H:%M:%S"))


# print(data_in_future(2))