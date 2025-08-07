

# import datetime
# # print(datetime.datetime)

# # now = datetime.datetime.now()
# # print("Current date and time:", now)

# # # create specific dates
# # birth_day = datetime.date(1990, 5, 15)
# # print("Birthday:", birth_day)    


# # # date math 
# # today = datetime.date.today()
# # age_days = today - birth_day
# # print("Days since birth day:", age_days.days)


# # # format dates
# # formatted_date = today.strftime("%Y-%m-%d")
# # print("Formatted date:", formatted_date)


# # # time deltas 
# # one_week = datetime.timedelta(days=7)
# # print("One week from today:", today + one_week)



# # json - java script object notation

# import json 
# # print(help(json))

# personal_data = {
#     "name": "Agatha", 
#     "age": 48, 
#     "skills": ["Drive", "Pay bills", "party"], 
#     "active": True
# }

# # convert to json string
# # json_string = json.dumps(personal_data)
# # print(json_string)
# # for string in json_string:
# #     print(string)

# # print(type(json_string))

# # convert back to python object
# # python_object = json.loads(json_string)
# # print(python_object)
# # print(type(python_object))
# # for key, value in python_object.items():
# #     print(f"{key}: {value}")


# # os module - operating system module
# import os
# # current_directory = os.getcwd()
# # # print("Current Directory:", current_directory)

# # files = os.listdir(current_directory)
# # # print(files)
# # # # print("Files in Current Directory:")
# # # for file in files:
# # #     print("-", file)


# # file_exists = os.path.exists("11_standard_library.py")
# # print(file_exists)


# # create a new directory
# data_dir = "data"
# if not os.path.exists(data_dir):
#     os.makedirs(data_dir)
#     print(f"Created directory: {data_dir}")
# else:
#     print(f"Directory '{data_dir}' already exists.")


# # create a new file in the data directory
# file_path = os.path.join(data_dir, "example.txt") # 'data/example.txt'
# print(file_path)
# with open(file_path, "w") as file:
#     file.write("This is an example file created using the os module.")
#     print(f"Created file: {file_path}")


# # sys module - system module
# import sys
# print("Python Version:", sys.version)
# print("Platform:", sys.platform)
# print("Executable Path:", sys.executable)


# Exercise 

# write a python program 
# 1. Gets the current date and time 
# 2. Calculates how many days, hours, and minutes until the next New Year's Eve (January 1st)


import datetime 

now = datetime.datetime.now()
# print(now)

new_year = datetime.datetime(now.year + 1, 1, 1)
# print(new_year)

# difference = new_year - now
days = new_year - now
# print(days)
# print(days.days)
# print(days.seconds)
print(type(days))
print(str(days))
str_days = str(days)
print(str_days.split())
print(str_days.split()[0])  # days
print(str_days.split()[:])  # hours
print(str_days.split()[2])  # minutes
min_split = str_days.split()[2]
print(min_split.split(":"))  # ['00', '00', '00']
print(min_split.split(":")[0])  # hours
print(min_split.split(":")[1])  # minutes
print(min_split.split(":")[2])  # seconds         


hours, remainder = divmod(days.seconds, 3600)
# print(hours, remainder)
minutes,seconds = divmod(remainder, 60)
# print(minutes, seconds)



# divmod - divides two numbers and returns a tuple of the quotient and remainder

# minutes, seconds = divmod(remainder, 60)

# print(f"Time until next New Year's Eve: {days.days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")