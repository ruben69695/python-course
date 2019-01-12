import datetime, time, os

while (True):
    os.system("clear")
    date = datetime.datetime.now()
    print("CLOCK\n{}:{}:{}".format(str(date.hour).rjust(2, "0"), str(date.minute).rjust(2, "0"), str(date.second).rjust(2, "0")))
    time.sleep(1.0)
