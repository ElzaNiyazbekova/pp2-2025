import datetime

start_str = input("Enter ")
start_date = datetime.datetime.strptime(start_str, "%Y-%m-%d")

end_str = input("Enter ")
end_date = datetime.datetime.strptime(end_str, "%Y-%m-%d")

time_diff = (end_date - start_date).total_seconds()

print( time_diff)

st = input