from datetime import datetime

# current_date_time = datetime.datetime.now()
# print(current_date_time)
current_date= datetime.now().date()
print(current_date)
current_time = datetime.now().time()
print(current_time)
new_year_eve = datetime(2025, 12, 31, 23, 59, 59)
print(f"Time until New Year's Eve: {new_year_eve - datetime.now()}")
