# name ="Alice"
# age = 30
# is_developer = True
# salary = 400000.00
# complex_datatype = salary + 4j

# print("Hello" + name + "!")
# print(type(complex_datatype))

# # prmitives in python are  int, str, float, boolean, complex
# print("your age is: "+ str(age))
# print(type(str(age)))
# print(f"My name is {name} age {age} old and type of complex is {type(complex_datatype)}")

# # Example of callable example
# def function(define):
#     if isinstance(define, int):
#         return 'sorry'
#     else:
#         return len(define)

# print(function(10))


# # Difference between def and class ( def can be used as function or method where as classes for creating objects)

# # function
# def double(x):
#     return x * 2

# # class
# class MyClass(object):
#     # method
#     def myMethod(self):
#         print ("Hello, World")

# myObject = MyClass()
# myObject.myMethod()  # will print "Hello, World"
# print(double(11))  # will print 22

# print("firstname", "lastname", "middlename", sep="--->")
# quote = "To be or not to be "
# print(quote.find("be"))
# print(quote.replace("be", "test"))
# print(quote)
# quote.upper()
# print(quote)

# print( quote and quote.upper())
# print (quote.lower() and quote)

# print(quote or quote.upper())
# print(quote.upper() and quote)

name = input("what is your name: ")
print (f"Hello my name is {name}")
age = input("what is your age? ")
print(f"My age is {age} and type of age is {type(age)}")
