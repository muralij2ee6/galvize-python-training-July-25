
# 🐍 Python Fundamentals – Full Review Tutorial

This tutorial covers Python fundamentals in depth. It's designed for review or code-along practice. Each section includes examples, method usage, and exercises.

---

## 1️⃣ Strings (`str`)

### 📌 What is a String?
A string is a sequence of characters wrapped in quotes.

```python
greeting = "Hello, world!"
```

### 🔧 String Methods

```python
text = "  hello python  "
print(text.upper())       # "  HELLO PYTHON  "
print(text.strip())       # "hello python"
print(text.replace(" ", "-"))  # "--hello-python--"
print("email@domain.com".split("@"))
print("-".join(["2024", "08", "01"]))
```

### 🧪 String Practice

```python
s = "banana"
print(s.count("a"))
print(s.startswith("ban"))
print(s.endswith("na"))
print(s[::-1])  # Reverse string
```

---

## 2️⃣ Integers & Floats (`int`, `float`)

```python
x = 10
y = 3.5

print(x + y)
print(x ** 2)
print(x // 3)     # Integer division
print(divmod(10, 3))  # (3, 1)
```

### 🔧 Useful Functions
```python
abs(-7)
round(3.14159, 2)
pow(2, 3)
```

---

## 3️⃣ Booleans (`bool`)

```python
is_admin = True
is_logged_in = False

print(is_admin and is_logged_in)
print(not is_logged_in)
```

---

## 4️⃣ Lists (`list`)

```python
tasks = ["email", "meeting", "code"]
tasks.append("lunch")
tasks.remove("meeting")
print(tasks[0])
```

### 🔧 List Methods

```python
numbers = [4, 1, 8, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))
```

---

## 5️⃣ Tuples (`tuple`)

```python
coords = (10, 20)
print(coords[0])
```

Tuples are immutable. You can’t change them after creation.

### 🔧 Tuple Unpacking

```python
x, y = coords
print(x, y)
```

---

## 6️⃣ Sets (`set`)

```python
langs = {"python", "javascript", "python"}
langs.add("go")
print(langs)
```

### 🔧 Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)  # Intersection
print(a | b)  # Union
print(a - b)  # Difference
```

---

## 7️⃣ Dictionaries (`dict`)

```python
user = {"name": "Alice", "age": 30}
print(user["name"])
user["email"] = "alice@example.com"
```

### 🔧 Dictionary Methods

```python
print(user.keys())
print(user.values())
print(user.items())
```

---

## 8️⃣ Control Flow

### 🔁 `if`, `elif`, `else`

```python
temp = 72

if temp > 80:
    print("Hot")
elif temp > 60:
    print("Nice")
else:
    print("Cold")
```

### 🔁 Loops

```python
# for loop
for i in range(3):
    print(i)

# while loop
x = 0
while x < 3:
    print(x)
    x += 1
```

---

## 9️⃣ Functions

```python
def greet(name="World"):
    return f"Hello, {name}!"

print(greet("Alice"))
```

### ➕ `*args`, `**kwargs`

```python
def add_all(*nums):
    return sum(nums)

def display(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
```

---

## 🔟 Classes

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True

task1 = Task("Study Python")
task1.mark_done()
print(task1.completed)
```

---

## 🔧 Python Standard Library

### 📆 datetime

```python
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

### 📁 File I/O

```python
with open("notes.txt", "w") as f:
    f.write("Hello file!")

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
```

### 🔄 JSON

```python
import json

data = {"name": "Alice"}
with open("data.json", "w") as f:
    json.dump(data, f)
```

---

## 🔄 Virtual Environments

```bash
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (bash)
venv/Scripts/activate
# Activate (macOS/Linux)
source venv/bin/activate
```

---

## 📦 Third-Party Libraries

### ✅ Install with pip

```bash
pip install requests pillow pyjokes
```

### 🤖 Using `pyjokes`

```python
import pyjokes
print(pyjokes.get_joke())
```

### 🖼️ Pillow Example

```python
from PIL import Image, ImageDraw

img = Image.new("RGB", (200, 100), "white")
draw = ImageDraw.Draw(img)
draw.text((10, 40), "Hi!", fill="black")
img.save("test.png")
```

---

## 🌐 Calling APIs

### Using `requests`

```python
import requests

response = requests.get("https://api.github.com")
if response.ok:
    data = response.json()
    print(data["current_user_url"])
```

---

## 📌 Exporting Dependencies

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

---

## 🧠 Practice Prompts

- Build a simple to-do CLI app with file save/load.
- Fetch NASA’s Astronomy Picture of the Day using `requests`.
- Create a note-taker using dictionaries and file I/O.

---

Happy coding! 🚀
