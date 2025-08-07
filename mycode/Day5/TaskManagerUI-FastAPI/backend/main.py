from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import uvicorn  # Add this import

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
conn = sqlite3.connect('tasks.db', check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    priority TEXT DEFAULT 'medium',
    completed BOOLEAN DEFAULT FALSE
)
''')
conn.commit()

# Pydantic model
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    priority: str = "medium"
    completed: bool = False

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Task Manager API is running"}

# Tasks endpoints
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return [dict(zip(['id', 'title', 'description', 'priority', 'completed'], task)) for task in tasks]

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    cursor.execute('''
    INSERT INTO tasks (title, description, priority, completed)
    VALUES (?, ?, ?, ?)
    ''', (task.title, task.description, task.priority, task.completed))
    conn.commit()
    task.id = cursor.lastrowid
    return task

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)