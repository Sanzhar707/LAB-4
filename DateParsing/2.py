from datetime import datetime, timedelta

current_date = datetime.now()
tomorrow = current_date + timedelta(days=1)
yesterday = current_date - timedelta(days=1)

print("Yesterday:", yesterday.strftime("%d-%m-%Y"))
print("Today:", current_date.strftime("%d-%m-%Y")) # strftime = string format time 
print("Tomorrow:", tomorrow.strftime("%d-%m-%Y"))