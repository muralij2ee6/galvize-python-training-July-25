# what is __name__ == "__main__" 

# Every python file (module) has a built in variable called __name__ 

# class Task:
#     pass 

# print(Task.__name__)

# __name__ == "__main__" 
# is a common Python idiom used to determine if a module is being run as the main program or if it is being imported into another module. When a Python file is executed, the interpreter sets the __name__ variable to "__main__". If the file is imported, __name__ is set to the module's name.


import calc

# print(calc)

print(calc.add(2, 3))


# __name__ == "__main__" 
# if i open this book direclty, start reading chapter 1
# i am refererncing this book from another, don't start reading automaticaly. 


# __name__ == "module_name" 