import datetime

x = datetime.datetime.now()
print(int(x.strftime("%d"))-1, ".", x.strftime("%m"))
print(int(x.strftime("%d")), ".", x.strftime("%m"))
print(int(x.strftime("%d"))+1, ".", x.strftime("%m"))