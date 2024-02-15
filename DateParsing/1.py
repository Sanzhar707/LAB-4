from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current date:", current_date.strftime("%d-%m-%Y")) # strftime = string format time 
print("5 days ago it was:", new_date.strftime("%d-%m-%Y"))