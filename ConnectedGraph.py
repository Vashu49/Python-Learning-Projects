#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx

def is_connected(graph):
    # Perform depth-first search from an arbitrary node
    start_node = next(iter(graph.nodes()))
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph.neighbors(node))

    # Check if all nodes are visited
    return len(visited) == len(graph.nodes())

def main():
    # Create a graph from user input
    edges = []
    print("Enter edges (format: node1 node2), type 'done' to finish:")
    while True:
        edge = input().strip()
        if edge.lower() == 'done':
            break
        node1, node2 = edge.split()
        edges.append((node1, node2))

    graph = nx.Graph()
    graph.add_edges_from(edges)

    # Check if the graph is connected
    connected = is_connected(graph)

    if connected:
        print("The graph is connected.")
    else:
        print("The graph is not connected.")

if __name__ == "__main__":
    main()


# In[ ]:




