#!/usr/bin/env python
# coding: utf-8

# In[2]:


import datetime

class Goal:
    def __init__(self, name, goal_type, target_amount=None, target_date=None, description="", priority="Medium"):
        self.name = name
        self.goal_type = goal_type
        self.target_amount = target_amount
        self.target_date = datetime.datetime.strptime(target_date, "%Y-%m-%d").date() if target_date else None
        self.description = description
        self.priority = priority
        self.progress = 0

    def update_progress(self, amount):
        if self.progress + amount <= self.target_amount:
            self.progress += amount
            return True
        else:
            return False

class GoalTracker:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        self.goals.append(goal)

    def track_progress(self, goal_name, amount):
        for goal in self.goals:
            if goal.name == goal_name:
                if goal.update_progress(amount):
                    print(f"Progress updated for goal '{goal_name}'.")
                else:
                    print(f"Goal '{goal_name}' already reached its target.")
                return
        print("Goal not found!")

    def view_goals(self):
        if not self.goals:
            print("No goals found.")
            return
        print("Goal Tracker:")
        for i, goal in enumerate(self.goals, start=1):
            print(f"{i}. {goal.name} - Type: {goal.goal_type}, Target Amount: {goal.target_amount}, Target Date: {goal.target_date}, Priority: {goal.priority}, Progress: {goal.progress}/{goal.target_amount}")

# Sample Goal Tracker
tracker = GoalTracker()

# Add goals to the tracker
goal1 = Goal("Save for Vacation", "Financial", 5000, "2024-12-31", description="Dream vacation to Europe")
goal2 = Goal("Run a Marathon", "Health", target_amount=26.2, description="Run the New York Marathon")
goal3 = Goal("Learn Python Programming", "Personal Development", description="Become proficient in Python")

tracker.add_goal(goal1)
tracker.add_goal(goal2)
tracker.add_goal(goal3)

# Update progress for goals
tracker.track_progress("Save for Vacation", 1000)
tracker.track_progress("Run a Marathon", 5)

# View goals in the tracker
tracker.view_goals()


# In[ ]:




