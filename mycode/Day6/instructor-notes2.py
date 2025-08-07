import json
import datetime
import os

tasks_data = [{
    "id": 1,
    "title": "Complete Python project",
    "completed": False,
    "created_at": datetime.datetime.now().isoformat()
},
    {
        "id": 2,
        "title": "Prepare for the meeting",
        "completed": True,
        "created_at": datetime.datetime.now().isoformat()
    }]

# save data to a JSON file

# def save_data_to_file(data, filename):
#     try:
#         with open(filename, 'w') as file:
#             json.dump(data, file, indent=4)
#             print(f"Data saved to {filename}")
#             return True
#     except Exception as e:
#         print(f"Error saving data to file: {e}")
#         return False

# save_data_to_file(tasks_data, 'tasks.json')


# save data to a JSON file (IF I NEVER WANT TO OVERWRITE THE FILE)

# def save_data_to_file(data, filename):
#     if not os.path.exists(filename):
#         try:
#             with open(filename, 'w') as file:
#                 json.dump(data, file, indent=4)
#                 print(f"Data saved to {filename}")
#             return True
#         except Exception as e:
#             print(f"Error saving data to file: {e}")
#         return False

# save_data_to_file(tasks_data, 'tasks.json')


# def load_data_from_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             print(f"Data loaded from {filename}")
#             print(data)
#             return data
#     except FileNotFoundError:
#         print(f"File {filename} not found.")
#         return None


# load_data_from_file('tasks.json')


# # create a new directory
# data_dir = "data"
# if not os.path.exists(data_dir):
#     os.makedirs(data_dir)
#     print(f"Created directory: {data_dir}")
# else:
#     print(f"Directory '{data_dir}' already exists.")

# lets create a app.py file inside the note_taker directory