import { useState, useEffect } from 'react'
import axios from 'axios'
import { PencilIcon, TrashIcon, CheckIcon } from '@heroicons/react/24/solid'

export default function TaskList() {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    const fetchTasks = async () => {
      const res = await axios.get('http://localhost:8000/tasks')
      setTasks(res.data)
    }
    fetchTasks()
  }, [])

  const getPriorityColor = (priority) => {
    switch(priority) {
      case 'high': return 'bg-red-100 border-red-500'
      case 'medium': return 'bg-yellow-100 border-yellow-500'
      case 'low': return 'bg-green-100 border-green-500'
      default: return 'bg-gray-100'
    }
  }

  const fetchTasks = async () => {
  try {
    const res = await axios.get('http://localhost:8000/tasks', {
      headers: {
        'Content-Type': 'application/json',
      }
    });
    setTasks(res.data);
  } catch (error) {
    console.error("Error fetching tasks:", error);
  }
};

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">My Tasks</h1>

      <div className="space-y-3">
        {tasks.map(task => (
          <div
            key={task.id}
            className={`p-4 rounded-lg border-l-4 ${getPriorityColor(task.priority)}`}
          >
            <div className="flex justify-between">
              <h3 className={`font-medium ${task.completed ? 'line-through' : ''}`}>
                {task.title}
              </h3>
              <div className="flex space-x-2">
                <button className="text-blue-500 hover:text-blue-700">
                  <PencilIcon className="h-5 w-5" />
                </button>
                <button className="text-red-500 hover:text-red-700">
                  <TrashIcon className="h-5 w-5" />
                </button>
                {!task.completed && (
                  <button className="text-green-500 hover:text-green-700">
                    <CheckIcon className="h-5 w-5" />
                  </button>
                )}
              </div>
            </div>
            {task.description && (
              <p className="mt-2 text-gray-600">{task.description}</p>
            )}
            {task.due_date && (
              <p className="mt-1 text-sm text-gray-500">
                Due: {new Date(task.due_date).toLocaleDateString()}
              </p>
            )}
          </div>
        ))}
      </div>
    </div>
  )
}