"""
Story 1: As a user, I want to add a new taks with a title SO that i can 
track what I need to do. 
    Acceptance Critera: 
        - User can input a task title 
        - Task is stored in local memory 
        - user receives a confirmation that task was added 

"""

print("====== Personal Task Manager")
print("Welcome to your personal task manager")

task1 = ""
task2 = ""
task3 = ""
task_count = 0

while True:    
    user_input = input("\n\nWhat would you like to do?\n1. Add a Task\n2. View a Task\n3. Exit\n")
    if(user_input=="1"):        
        print("\n --- Adding your First Task")
        print("="+30)
        task_title= input("Enter your the first task: ")
        print("\n" + "="*30)
        task_title = task_title.strip()
        if (len(task_title))> 0 :
            task1 = task_title
            task_count += 1
            print(f"Task : {task1} has been added sucessfully !")            
            task_title = input("Enter your the second task: ")
            task2 = task_title
            task_count += 1
            print(f"Task : {task2} has been added sucessfully !")            
            task_title = input("Enter your the Third task: ")
            task3 = task_title
            task_count += 1
            print(f"Task : {task3} has been added sucessfully !")
            print(f"Total task count is {task_count}")            
        else:
            print(f" Task count cant be empty {task_count}, please try again")
        user_input = input("What would you like to do? \n1. Add a Task\n2. View a Task\n3. Exit\n")
    if(user_input=="2"):
        print("\n==== Display of all tasks ====")
        print(f"Task1 : {task1}")
        print(f"Task2 : {task2}")
        print(f"Task3 : {task3}")
        print("===========================================")
    else:
        break

