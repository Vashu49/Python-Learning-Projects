#!/usr/bin/env python
# coding: utf-8

# In[1]:


import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    # Set distance to start node as 0
    distances[start] = 0

    # Initialize priority queue
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        # Pop node with smallest distance from priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # If current distance to current node is greater than the calculated distance, skip
        if current_distance > distances[current_node]:
            continue

        # Check each neighbor of current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If new distance is shorter than the stored distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node, ":")
for node, distance in shortest_distances.items():
    print(f"To node {node}: {distance}")


# In[ ]:




