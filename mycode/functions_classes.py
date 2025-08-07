# def obect(name, emoji):
#     return name, emoji
# print(type(obect("apple", 1)))


class Person:
    def __init__(self, name):
        self.name = name

def print_names(*args):
    for obj in args:
        print(obj.name)

person1 = Person("Alice")
person2 = Person("Bob")

# Passing objects as *args
print_names(person1, person2)

def describe_objects(*args):
    for obj in args:
        print(f"Type: {type(obj)}, Value: {obj}")

describe_objects(42, "hello", [1, 2, 3], Person("Charlie"))

#Yes, You Can Pass Objects to **kwargs

class Car:
    def __init__(self, model):
        self.model = model

def print_car_details(**kwargs):
    for key, value in kwargs.items():
        if hasattr(value, 'model'):  # Check if the object has a 'model' attribute
            print(f"{key}: {value.model}")
        else:
            print(f"{key}: {value}")

car1 = Car("Tesla Model S")
car2 = Car("Ford Mustang")

# Passing objects as **kwargs
print_car_details(
    electric_car=car1,
    muscle_car=car2,
    year=2023,
    color="red"
)

# Key Points:
# **kwargs collects keyword arguments into a dictionary ({key: value}).
#
# The value can be any Python object (instances, primitives, functions, etc.).
#
# You can check object attributes/methods inside the function (e.g., using hasattr() or isinstance()).


def inspect_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value} (Type: {type(value)})")

inspect_kwargs(
    num=42,
    text="hello",
    my_list=[1, 2, 3],
    my_car=Car("Porsche"),
    my_func=print  # Even functions are objects!
)
# Output:
# num: 42 (Type: <class 'int'>)
# text: hello (Type: <class 'str'>)
# my_list: [1, 2, 3] (Type: <class 'list'>)
# my_car: <__main__.Car object at 0x...> (Type: <class '__main__.Car'>)
# my_func: <built-in function print> (Type: <class 'builtin_function_or_method'>)

class Car:
    # Static variable (class variable)
    wheels = 4

    def __init__(self, brand):
        self.brand = brand  # Instance variable

# Accessing static variable
print(Car.wheels)  # Output: 4

# Creating objects
car1 = Car("Toyota")
car2 = Car("BMW")

print(car1.wheels)  # Output: 4 (accessed via instance)
print(car2.wheels)  # Output: 4

class Car:
    wheels = 4

car1 = Car()
car2 = Car()

# Modify via class (affects all instances)
Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6

# Modify via instance (creates a new instance variable)
car1.wheels = 8
print(car1.wheels)  # 8 (instance variable)
print(car2.wheels)  # 6 (still uses class variable)

# 4. Static Variables                           vs. Instance Variables
# Feature	Static Variable (Class.var)	        Instance Variable (self.var)
# Scope	Shared across all instances	            Unique to each instance
# Memory	Stored once per class	            Stored per instance
# Modification	Affects all instances	        Affects only one instance

# Example of static variable in a class

# Mutable Static Variable)

class ShoppingCart:
    items = []  # Static list (shared across all instances)

    def add_item(self, item):
        self.items.append(item)

cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.add_item("Apple")
cart2.add_item("Banana")

print(cart1.items)  # ['Apple', 'Banana'] (shared list!)

# Avoid mutable statics or initialize in __init__:

class ShoppingCart:
    def __init__(self):
        self.items = []  # Now instance-specific

# Static Methods

# If you want a method that doesn’t depend on instance/class state, use @staticmethod:
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(2, 3))  # Output: 5 (no instance needed)

