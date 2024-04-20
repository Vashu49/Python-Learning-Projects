#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Job:
    def __init__(self, title, company, location, description):
        self.title = title
        self.company = company
        self.location = location
        self.description = description

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.applied_jobs = []

    def apply_for_job(self, job):
        self.applied_jobs.append(job)
        print(f"{self.username} applied for the job: {job.title} at {job.company}")

class JobPortal:
    def __init__(self):
        self.jobs = []
        self.users = []

    def post_job(self, job):
        self.jobs.append(job)
        print(f"Job posted: {job.title} at {job.company}")

    def search_jobs(self, keyword, location=None):
        found_jobs = []
        for job in self.jobs:
            if keyword.lower() in job.title.lower() or keyword.lower() in job.description.lower():
                if location:
                    if location.lower() == job.location.lower():
                        found_jobs.append(job)
                else:
                    found_jobs.append(job)
        if found_jobs:
            print(f"Found {len(found_jobs)} jobs matching '{keyword}':")
            for job in found_jobs:
                print(f"{job.title} at {job.company}, Location: {job.location}")
        else:
            print("No jobs found matching the keyword.")

    def register_user(self, username, email, password):
        new_user = User(username, email, password)
        self.users.append(new_user)
        print(f"User '{username}' registered successfully.")
        return new_user

    def authenticate_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                print(f"User '{user.username}' authenticated successfully.")
                return user
        print("Authentication failed. Invalid email or password.")
        return None

# Sample usage
if __name__ == "__main__":
    # Creating a job portal
    job_portal = JobPortal()

    # Posting some sample jobs
    job1 = Job("Software Engineer", "ABC Inc.", "New York", "Looking for a software engineer with Python skills.")
    job2 = Job("Data Analyst", "XYZ Corp.", "San Francisco", "Seeking a data analyst proficient in SQL and Excel.")
    job3 = Job("Web Developer", "123 Tech", "Chicago", "Hiring a web developer experienced in HTML, CSS, and JavaScript.")
    job_portal.post_job(job1)
    job_portal.post_job(job2)
    job_portal.post_job(job3)

    # Registering new users
    user1 = job_portal.register_user("user1", "user1@example.com", "password123")
    user2 = job_portal.register_user("user2", "user2@example.com", "password456")

    # Authenticating users
    authenticated_user = job_portal.authenticate_user("user1@example.com", "password123")

    if authenticated_user:
        # User applying for jobs
        authenticated_user.apply_for_job(job1)

    # Searching for jobs
    job_portal.search_jobs("software")


# In[ ]:




