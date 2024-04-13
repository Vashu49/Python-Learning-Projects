#!/usr/bin/env python
# coding: utf-8

# In[4]:


def sieve_of_eratosthenes(limit):
    # Create a boolean list "prime[0..limit]" and initialize all entries as True
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    p = 2
    while p * p <= limit:
        # If primes[p] is still True, then it is a prime
        if primes[p]:
            # Update all multiples of p
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    # Print all prime numbers
    prime_numbers = [i for i in range(2, limit + 1) if primes[i]]
    return prime_numbers

limit = 10000000  # Adjust the limit as needed
primes_below_limit = sieve_of_eratosthenes(limit)
print("Prime numbers below", limit, "are:", primes_below_limit)


# In[15]:


def sieve_of_eratosthenes(limit):
    # Create a boolean list "prime[0..limit]" and initialize all entries as True
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    p = 2
    while p * p <= limit:
        # If primes[p] is still True, then it is a prime
        if primes[p]:
            # Update all multiples of p
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    # Collect all prime numbers
    prime_numbers = [i for i in range(2, limit + 1) if primes[i]]
    return prime_numbers

# Get the limit from the user
limit = int(input("Enter the limit to find prime numbers up to: "))
primes_below_limit = sieve_of_eratosthenes(limit)
print("Prime numbers below", limit, "are:", primes_below_limit)


# In[3]:


def sieve_of_eratosthenes(limit):
    # Create a boolean list "prime[0..limit]" and initialize all entries as True
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    p = 2
    while p * p <= limit:
        # If primes[p] is still True, then it is a prime
        if primes[p]:
            # Update all multiples of p
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    # Collect all prime numbers
    prime_numbers = [i for i in range(2, limit + 1) if primes[i]]
    return prime_numbers

limit = 10000000  # Adjust the limit as needed
primes_below_limit = sieve_of_eratosthenes(limit)
print("Number of prime numbers below", limit, "is:", len(primes_below_limit))


# In[5]:


import math

def distance(point1, point2):
    # Euclidean distance between two points
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair_brute_force(points):
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance

# Example usage
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
closest_pair, min_distance = closest_pair_brute_force(points)
print("Closest pair:", closest_pair, "with distance:", min_distance)


# In[13]:


import math

def distance(point1, point2):
    # Euclidean distance between two points
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair_brute_force(points):
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance

# Example usage with user input
num_points = int(input("Enter the number of points: "))
points = []
for i in range(num_points):
    while True:
        try:
            coordinates = input(f"Enter the coordinates of point {i + 1} (x y): ")
            x, y = map(int, coordinates.split())
            points.append((x, y))
            break
        except ValueError:
            print("Invalid input format. Please enter two integers separated by a space.")

closest_pair, min_distance = closest_pair_brute_force(points)
print("Closest pair:", closest_pair, "with distance:", min_distance)


# In[ ]:




