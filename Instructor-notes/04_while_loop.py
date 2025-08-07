# while loop 

# while condition: 
    #     do something
# the loop runs until the condition becomes false
# you must make sure the condition eventually becomes false, otherwise it will run indefinitely - into an infinite loop

# count = 1

# while count <= 5:
#     print(f"Count is: {count}")
#     count += 1  # Increment count by 1

# print("Loop has ended.")  # This will execute after the loop ends


# # user input 

# password = ""
# while password != "python123":
#     password = input("Enter the password: ")

# print("Access granted!")  # This will execute after the correct password is entered

# break 

# number = 1

# while True:
#         print(f"Current number is: {number}")
#         if number == 3:
#                 print("breaking point of the loop")
#                 break 
#         number += 1  # Increment number by 1


# continue 

number = 0

while number < 5:
    number += 1  # Increment number by 1
    if number == 3:
        print("Skipping number 3")
        continue  # Skip the rest of the loop for this iteration
    print(f"Current number is: {number}")





