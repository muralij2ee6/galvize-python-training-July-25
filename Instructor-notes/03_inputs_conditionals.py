# getting user input


name = input("What is your name? ")
# conditionals with strings 
if len(name) > 0:
    print(f"Nice to meet you, {name}!")
    print(f"Hello, {name}!")
    age = input("what is your age?")
    print(f"You are {age} years old.")
    age = int(age)
    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
else:
    print("You didn't provide a name.")
    name = input("What is your name? ")


  # Convert age to an integer
# print(f"You are {type(age)} years old.")





# basic conditional logic
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")


# Conditional logic with multiple conditions
