#!/usr/bin/env python
# coding: utf-8

# In[1]:


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

class VotingSystem:
    def __init__(self):
        self.users = {}  # Store users with username as key
        self.candidates = []  # Store candidates

    def register_user(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password)
            print(f"User '{username}' registered successfully.")
        else:
            print(f"Username '{username}' already exists. Please choose a different username.")

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def register_candidate(self, candidate_name):
        candidate = Candidate(candidate_name)
        self.candidates.append(candidate)
        print(f"Candidate '{candidate_name}' registered successfully.")

    def vote(self, candidate_name):
        for candidate in self.candidates:
            if candidate.name == candidate_name:
                candidate.votes += 1
                print(f"Voted for '{candidate_name}'.")
                return
        print(f"Error: Candidate '{candidate_name}' not found.")

    def tally_votes(self):
        print("Vote Tally:")
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes} votes")

# Example usage:
voting_system = VotingSystem()

# Register users
voting_system.register_user("user1", "password1")
voting_system.register_user("user2", "password2")

# Login
voting_system.login("user1", "password1")

# Register candidates
voting_system.register_candidate("Narendra Modi")
voting_system.register_candidate("Rahul Gandhi")

# Vote
voting_system.vote("Narendra Modi")
voting_system.vote("Rahul Gandhi")
voting_system.vote("NOTA")

# Tally votes
voting_system.tally_votes()


# In[ ]:




