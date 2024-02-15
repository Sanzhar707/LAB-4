from datetime import datetime

date_1 = input("Enter the first date (DD-MM-YYYY HH:MM:SS): ")
date_2 = input("Enter the second date (DD-MM-YYYY HH:MM:SS): ")

date1 = datetime.strptime(date_1, "%Y-%m-%d %H:%M:%S") #strptime создает дату с моего внесения
date2 = datetime.strptime(date_2, "%Y-%m-%d %H:%M:%S")

time_difference = date2 - date1

difference_in_seconds = time_difference.total_seconds()

print(f"The difference between the two dates is {difference_in_seconds} seconds.")
