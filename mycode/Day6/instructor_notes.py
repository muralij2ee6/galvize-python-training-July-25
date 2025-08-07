# Exception Handling Demo


# exception handling in python is done using try/except blocks

# indexError - trying to access an index that doesn't exist
# assertionError - raised when an assert statement fails
# attiributeError - trying to access an attribute that doesn't exist
# importError - trying to import a module that doesn't exist
# typeError - trying to perform an operation on a value of the wrong type
# valueError - trying to convert a value to a type that is not compatible
# zeroDivisionError - trying to divide by zero
# nameError - trying to access a variable that doesn't exist

class MyCustomError(Exception):
    """Custom exception for demonstration purposes."""
    pass


class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""

    def __init__(self, number):
        super().__init__(f"Negative number error: {number} is not allowed.")
        self.number = number


def fifty_by(number):
    # if number == 0:
    #     raise ZeroDivisionError("Cannot divide by zero!")
    try:
        if number == 1:
            raise MyCustomError
        if number < 0:
            raise NegativeNumberError(number)
        return 50 / number
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except MyCustomError:
        return "in execpt statement Error: Number cannot be 1!"
    except NegativeNumberError:
        return f"Error: {number} is a negative number!"


print(fifty_by(0))
print(fifty_by(1))
print(fifty_by(-5))

# print(help(ZeroDivisionError))

# banking

# class InsufficientFundsError(Exception):
#     """Custom exception for insufficient funds."""
#     # constructo init
#     # balance, amount

#     # method to make a message

#     # method for deficit value
#     # return how much amount mmore money is needed to cover the deficit
#     # self.amount - self.balance

#     # suggested action method
#     # consider depositing more money or withdrawing less


# except InsufficientFundsError as e::
#     print(f"Error: {e} {e.deficit_value()} is needed to cover the deficit. Consider depositing more money or withdrawing less.")



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