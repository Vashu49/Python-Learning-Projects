#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Task:
    def __init__(self, title, due_date, priority, category):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("Todo List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.title} (Due: {task.due_date}, Priority: {task.priority}, Category: {task.category}, Completed: {task.completed})")

# Create a sample Todo List
todo_list = TodoList()

# Add tasks to the Todo List
task1 = Task("Complete project proposal", "2024-04-20", "High", "Work")
task2 = Task("Buy groceries", "2024-04-15", "Medium", "Personal")
task3 = Task("Call John", "2024-04-18", "Low", "Personal")

todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)

# View tasks in the Todo List
todo_list.view_tasks()


# In[ ]:




