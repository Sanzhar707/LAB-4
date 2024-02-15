from datetime import datetime, timedelta

now = datetime.now()

microsec = int(input("Input microseconds: "))

delta = timedelta(microseconds=microsec)

new_time = now - delta

print(f"{microsec} microseconds ago: ", new_time.strftime("%f-%d-%m-%Y"))