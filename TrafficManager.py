#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import random

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        # Simulate vehicle movement
        time.sleep(0.1 / self.speed)

class TrafficSignal:
    def __init__(self):
        self.state = "green"

    def change_state(self):
        # Change signal state
        self.state = "red" if self.state == "green" else "green"
        print(f"Signal changed to {self.state}")

class TrafficSimulation:
    def __init__(self, road_length, num_vehicles):
        self.road_length = road_length
        self.num_vehicles = num_vehicles
        self.vehicles = [Vehicle(random.randint(1, 5)) for _ in range(num_vehicles)]
        self.signal = TrafficSignal()

    def simulate(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            # Move vehicles
            for vehicle in self.vehicles:
                vehicle.move()

            # Check traffic conditions and adjust signal
            if len(self.vehicles) > self.road_length / 2:
                self.signal.change_state()

if __name__ == "__main__":
    simulation = TrafficSimulation(10, 10)  # Road length: 10 units, 10 vehicles
    simulation.simulate(10)  # Simulate traffic for 10 seconds


# In[ ]:




