# # # classes in Python 



# # # print(help(list))
# # # print(dir(list))
# # # print(list.__doc__)
# # # print(list.__mro__)

# # # dunder methods
# # # __init__ - constructor method
# # # __str__ - string representation of the object
# # # __repr__ - official string representation of the object
# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.name = name  # instance variable
# # #         self.age = age    # instance variable
    
# # #     def introduuce(self):
# # #         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# # #     def __str__(self):
# # #         return f"This is an instance of the original Person class with {self.name}, who is {self.age} years old "
    
# # #     def has_birthday(self):
# # #         self.age += 1
# # #         return f"Happy Birthday {self.name}! You are now {self.age} years old."


# # # # print(dir(Person))
# # # print(Person)

# # # person1 = Person("Alice", 30)
# # # # print(person1.name)  # <__main__.Person object at 0x...>
# # # # print(person1.introduuce())  # Hello, my name is Alice and I am 30 years old.

# # # print(person1.has_birthday())


# # class Dog: 
# #     dog_id = 1  # class variable shared by all instances
# #     def __init__(self, name, age=0):
# #         self.name = name 
# #         self.age = age
# #         self.id = Dog.dog_id  # instance variable unique to each instance
# #         Dog.dog_id += 1  # increment class variable for next instance
    
# #     def __str__(self):
# #         return f"{self.name} is a {self.age} year old dog with ID {self.id}."
    
# #     def bark(self):
# #         return f"{self.name} says Woof!"
    
# #     @classmethod
# #     def get_total_dogs(cls):
# #         return Dog.dog_id - 1
    
# #     @staticmethod
# #     def is_dog(obj):
# #         return isinstance(obj, Dog)
    

# # dog1 = Dog("Remy", 3)
# # print(dog1)
# # dog2 = Dog("Joey", 10)
# # print(dog2)
# # dog3 = Dog("Tobi", 5)
# # print(dog3)


# # print(Dog.get_total_dogs())  # Accessing class method directly from the class
# # print(Dog.is_dog(dog1))  # Checking if dog1 is an instance of Dog

# # # Instance Methods 
# # # first argument is always self
# # # if it needs data from the specific object instance



# # # Static Methods 
# # # which use the decorator @staticmethod
# # # do not take self or cls as the first argument
# # # they are used for utility functions that do not need access to instance or class variables
# # # for example, a method that checks if an object is a Dog instance
# # # or helper funciton like addition  - related to the class but not dependent on instance or class variables

# # # if its just a helper that doesnt care about object or class state, use static method


# # # Class Methods
# # # which use the decorator @classmethod
# # # take cls as the first argument
# # # they are used for factory methods or methods that need to access class variables
# # # if it works on the class as a whole (tracking all instances, creating new instances, etc.), use class method





# class Task: 
#     # class attribute to keep track of tasks created 
#     total_tasks_created = 0 

#     def __init__(self, title, priority="2", completed=False):
#         # instance attributes
#         Task.total_tasks_created += 1  # increment total tasks created
#         self.id = Task.total_tasks_created  # unique ID for each task
#         self.title = title.strip()  # store task title, removing leading/trailing spaces
#         self.priority = priority  # store task priority
#         self.completed = completed  # task is not completed by default

#     def mark_complete(self):
#         self.completed = True  # mark task as completed
#         return f"Task #{self.id} '{self.title}' marked as complete!"
    
#     def __str__(self):
#         status = "✓ Complete" if self.completed else "○ Pending"
#         return f"Task #{self.id}: {self.title} | Priority: {self.priority} | Status: {status}"
    

# #task objects 
# task1 = Task("Learn Python", "1")
# task2 = Task("Complete Project")

# # print(task1)  # Task #1: Learn Python | Priority: 1 | Status: ○ Pending
# # print(task2)  # Task #2: Complete Project | Priority: 2 | Status: ○ Pending

# # print(task1.mark_complete())  # Task #1 'Learn Python' marked as complete!
# # print(task1)

# # OOP - thinking 
# # need to seperate behavior and data 
# # Task class to encapsulate task-related data and behavior

# # subclass adds a deadline attritube and overrides the __str__ method to include the deadline in the string representation

# from datetime import date
# # print(date.today())

# class DeadlineTask(Task):
#     def __init__(self, title, due_date, priority="2"):
#         # call the parent constructor to initialize common attributes
#         super().__init__(title, priority)
#         self.due_date = due_date  # store the due date for the task

#     def is_overdue(self):
#         return date.today() > self.due_date
    
#     # override the __str__ method to include the due date
#     def __str__(self):
#         base_str = super().__str__()  # get the base string from Task class
#         over_due_flag = " (Overdue)" if self.is_overdue() else "on time!"
#         return f"{base_str} | Due Date: {self.due_date} {over_due_flag}"
    
# task4 = DeadlineTask("Submit Assignment", date(2025, 10, 15), "1")
# print(task4)  # Task #3: Submit Assignment | Priority: 1 | Status: ○ Pending | Due Date: 2025-10-15 on time!

# task5 = DeadlineTask("fill out taxes", date(2025, 6, 15), "2")
# print(task5)
# print(task5.mark_complete())
# # print(task5)

# 1 composition - using other classes as attributes

# class Engine: 


# class Car:  


# 2. Aggregation - a looser form of composition where the contained object can exist independently of the container

# class Student: 


# class Course: 

    # many to many relationship


# 3. Association (classes talk via references) - a relationship where one class uses another class but does not own it


# class Teacher: 

# class Course:
#  classes collaborate but dont manage each other's lifecycle 



# # 4. dependency injection 

# class EmailSerivce: 

# class Notification



# # 5 callbacks / event systems 
# class button 
#     click 


# class some action 
    
