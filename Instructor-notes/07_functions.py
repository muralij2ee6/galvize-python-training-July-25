# # functions 

# # print(type(print))

# # () - # () - calling a function


# # def object():
# #     return "I am sometimes not properly defined"

# # object_dictionary = {
# #     "object": object()
# # }

# # print(object_dictionary)

# # def say_whatsup(name, emoji):
# #     # print(name, emoji)
# #     return name, emoji

# # print(type(say_whatsup("Bruce", "👋")))
# # say_whatsup("Bruce", "👋")

# # def create_tasks(task_title, task_id):
# #     # Create a new task dictionary
# #     # this function also will do x
# #     pass 


# # def show_tasks():
# #     # Show all tasks using iteration
# #     pass


# # some_list = ["A", "B", "C", "A", "B", "C"]
# # another_list = ["D", "B", "E", "D", "F"]

# # # function that checks for duplicates in two lists
# # # we want to return a new list of the duplicates
# # def find_duplicates(list1, list2):
# #     duplicates = [] 
# #     # lets join both the lists first
# #     combined_list = list1 + list2
# #     # print(combined_list)
# #     # now lets iterate through the combined list
# #     for item in combined_list:
# #         # if the item appears more than once in the combined list
# #         if combined_list.count(item) > 1:
# #             # and if it is not already in the duplicates list
# #             if item not in duplicates:
# #                 duplicates.append(item)
# #     return duplicates

# # find_duplicates(some_list, another_list)
# # print(find_duplicates(some_list, another_list))  # Output: ['A', '


# # output = ["A", "B", "C", "D"]




# # function with parameters and return value 
# # 

# # def greet_with_emoji(name, emoji="👋"):
# #     """
# #     This function greets a person with a specified emoji.
    
# #     Parameters:
# #     name (str): The name of the person to greet.
# #     emoji (str): The emoji to use in the greeting. Default is "👋".
    
# #     Returns:
# #     str: A greeting message.
# #     """
# #     return f"Hello {name} {emoji}"

# # print(greet_with_emoji("Alice", ":)"))  # Output: Hello Alice 👋


# # *args and **kwargs
# # *args allows you to pass a variable number of positional arguments to a function.
# # **kwargs allows you to pass a variable number of keyword arguments to a function.

# # Rule: The order of your parameters matter. 
# # params: positional, *args, default/keyword, **kwargs

# # def arg_demo(pos1, pos2, *args, color="blue", **kwargs):
# #     print(f"Positional 1: {pos1}, Positional 2: {pos2}")
# #     print(f"Args: {args}")
# #     print(type(args))  # Output: <class 'tuple'>
# #     for arg in args:
# #         print(f"Arg: {arg}")
# #     print(f"Color: {color}")
# #     print("Keyword Arguments:")
# #     for key, value in kwargs.items():
# #         print(f"{key}: {value}")



# # arg_demo("A", "B", "C", "D", "E", "F",size=10, shape="circle")

# # def log_habit(name, *days, **details):
# #     print(f"Habit Name: {name}")
# #     print("Days:", days)
# #     for day in days: # loops through the tuple of days
# #         print(f"Day: {day}")
# #         for i in day: # loops throughthe list 
# #             print(i)
# #     print("Details:", details)
# #     for key, value in details.items():
# #         print(f"{key}: {value}")

# # log_habit("Exercise", ["Monday", "Wednesday", "Friday"], duration="30 minutes", type="Cardio")



# # scope 
# # 1. local scope 
# # 2. global scope
# # 3. built-in scope
# # 4. nonlocal scope (used in nested functions)


# def say_hello():
#     name = "Alice"  # Local variable
#     print(f"Hello, {name}!")  # Accessing local variable


# # print(name) ## say_hello()  # This will raise an error because 'name' is not defined in the global scope

# def outer_function():
#     outer_var = "I am outside!"  # Outer function variable
#     print(inner_var)  # This will raise an error because inner_var is not defined in this scope

#     def inner_function():
#         inner_var = "I am inside!"  # Inner function variable
#         print(outer_var)  # Accessing outer function variable
#         print(inner_var)  # Accessing inner function variable

#     inner_function()  # Calling inner function

# outer_function()  # Calling outer function to see the output



# gloabal_var = "I am global!"  # Global variable

# def party():
#     another_var = "I am local!"  # Local variable
#     print(gloabal_var)  # Accessing global variable

# print(another_var)  # This will raise an error because 'another_var' is not defined in the global scope


# # Rule : LEGB - Local, Enclosing, Global, Built-in


# built in scope 

# print(len("Hello"))  # Using built-in function 'len' to get the length of a string

# def len(string):
#     # return - returns an int of the numer of characters in the string.

# built in fucntions - max, len, min, sum, sorted, print, type, input

# enclosing scope 


# def outer_function():
#     outer_var = "I am outside!"  # Outer function variable

#     def inner_function():
#         inner_var = "I am inside!"  # Inner function variable
#         print(outer_var)  # Accessing outer function variable
#         print(inner_var)  # Accessing inner function variable

#     inner_function()  # Calling inner function

# outer_function()


# outer_var = "I am outside!"
# print(outer_var)  # Accessing outer function variable
# print(inner_var)  # Accessing inner function variable
# inner_var = "I am inside!"
# inner_function():
# outer_function()
#     # callstack 


# function that validates input
# def get_valid_input(prompt, valid_options):
#     while True:
#         user_input = input(prompt).strip().lower()
#         if user_input in valid_options:
#             return user_input
#         else:
#             print(f"Invalid input! Please choose from: {', '.join(valid_options)}")

# get_valid_input("Enter your choice (1, 2, or 3): ", ["1", "2", "3"])


# function that processes lists 

def filter_and_sort_tasks(tasks, show_completed=None):
    # filter tasks 
    if show_completed is None: 
        filtered = tasks[:] # all tasks
    else:
        filtered = [task for task in tasks if task["completed"] == show_completed]
        # filtered = []
        # for task in tasks:
        #     if task["completed"] == show_completed:
        #         filtered.append(task)

    # sort by proitity(high=1, medium=2, low=3)
    sorted_tasks = sorted(filtered, key=lambda task: int(task.get("priority", 2)))  # Default priority is medium (2)
    return sorted_tasks

sample_tasks = [
    {"id": 1, "title": "Task 1", "completed": False, "priority": 1},
    {"id": 2, "title": "Task 2", "completed": True, "priority": 3},
    {"id": 3, "title": "Task 3", "completed": False, "priority": 2}
]
filtered_tasks = filter_and_sort_tasks(sample_tasks, show_completed=True)
print(filtered_tasks)