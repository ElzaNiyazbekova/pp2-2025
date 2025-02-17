import datetime

x = datetime.datetime.now()
print(int(x.strftime("%d"))-5, ".", x.strftime("%m"))