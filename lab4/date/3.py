import datetime

x = datetime.datetime.now()
print((x.strftime("%d"))+"."+(x.strftime("%m"))+'.'+x.strftime("%H")+'.'+(x.strftime("%M"))+"."+x.strftime("%S"))