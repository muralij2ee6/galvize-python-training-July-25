fruits = ["apples", "banana", "cherries", "kiwi", "peaches"]
copy_of_fruits = fruits[:]
# fruits.extend("mango", "pinnaple")
# list unpacking
a, b, c, *other, d = ["1", 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a, b, c, other, d)
print(type(a))
print(type(other))

#range
# print(list(range(1, 11)))
# for i in range (1,11):
#     print(i, end=" ")

#Swapping values
a, b = 10, 20
a, b = b, a
print(f"a is {a} b is {b}")

# enumarate() - used to get index and value in loop
my_list = ["apple", "banana", "cherry"]
for index, value in enumerate(my_list):
    print(f"Index: {index+1}, Value: {value}")
    
# #tuples - immutable lists
# my_tuple = (1, 2, 3, 4, 5)
# # print(my_tuple[0])  # Accessing tuple element
# my_tuple[1]= 20  # This will raise an error because tuples are immutable
#zip methos
# zip() - combines two or more lists into a list of tuples
list1 = [1, "2", "3"]   
list2 = ['a', 'b']
zipped = list(zip(list1, list2))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# containers - lists, tuples, dictionaries, sets
# for loops, while loops, break, continue
# list comprehensions
# work with enumerate(), zip(), map(), filter(), reduce(), range()

# lists --- []
# - ordered, mutable, indexed by position 

fruits = ["apple", "banana", "cherry", "peaches", "kiwi"]
# print(fruits[0])  # Accessing first element
# print(fruits[-1])
# # print(fruits(-2)) # list is not a callable object

# print(len(fruits))  # Length of the list

# # list slicing - [start:end:step]
# print(fruits[1:3])  # Slicing from index 1 to 2
# print(fruits[:3])  # Slicing from start to index 2
# print(fruits[2:])  # Slicing from index 2 to end
# print(fruits[::2])  # Slicing with step of 2

# copy_of_fruits = fruits[:]  # Copying the list
# print(copy_of_fruits == fruits)  # True, both lists are equal
# print(copy_of_fruits is fruits)  # False, they are different objects


# adding and removing elements
# fruits.append("orange")  # Adding an element to the end
# print(fruits)

# fruits.remove("banana")  # Removing an element by value
# print(fruits)


# fruits.insert(1, "grape")  # Inserting an element at index 1
# print(fruits)

# fruits.extend(["mango", "pineapple"])  # Extending the list with another list
# print(fruits)


# popped_item = fruits.pop()  # Removing the last element
# print(fruits)
# print(f"Popped item: {popped_item}")  # Displaying the popped item


# fruits.clear()  # Clearing the list
# print(fruits)  # Should be an empty list

# my_string = "Hello, World!"
# # Converting string to list of characters
# char_list = list(my_string)
# print(char_list)  # ['H', 'e', 'l', 'l', '

# # my_string.split(", ")  # Splitting string into a list
# print(my_string.split(", "))  # ['Hello', 'World!']


# list unpacking 

# a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
# # print(a, b, c, other, d)  

# # range()
# ## range(start, stop, step)
# # print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in range(11, 0, -2):
#     print(number)  # This will not print anything because step is negative and start is less than stop

# numbers = list(range(1, 11))  # Creating a list of numbers from 1 to 10
# print(numbers)


# num = 5
# print("multiplication table of", num)

# for i in range(1, 101):
#     print(f"{num} x {i} = {num * i}")  # Printing multiplication table of num


# import time 

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)  # Pausing for 1 second
# print("Time is up! Be happy!")


# rows = 5
# for i in range(1, rows + 1):
#     print("* " * i)  # Printing a right-angled triangle pattern


# list unpacking part 2

# one practical - ignore some values 

# data = ["Alice", 30, "Engineer", "New York"]

# name, age, *_, city = data 
# print(f"Name: {name}, Age: {age}, City: {city}")  # Output: Name: Alice, Age: 30, City: New York

# task_logs = [("Task1", True), ("Task2", False), ("Task3", True)]
# for task, status in task_logs:
#     status = "Completed" if status else "Not Completed"
#     print(f"{task}: {status}")  # Output: Task1: Completed, Task

# a, b, = 10, 20 
# a, b, = b, a  # Swapping values
# print(f"a: {a}, b: {b}")  # Output: a:



# # enumerate() - used to get index and value in a loop

# my_list = ["apple", "banana", "cherry"]
# for index, value in enumerate(my_list):
#     print(f"Index: {index+1}, Value: {value}")  # Output: Index: 0, Value: apple, etc.


# # tuples - immutable lists

# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple[0])  # Accessing first element
# # my_tuple[1] = "orange"  # This will raise an error because tuples are immutable

# zip() - combines two or more lists into a list of tuples
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c"]
zipped = list(zip(list1, list2))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]