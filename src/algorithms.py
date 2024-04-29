"""
Implementation of the Floyd-Warshall algorithm and related functions for the Streamlit app.

This module provides the implementation of the Floyd-Warshall algorithm, which is used to compute
the shortest paths between all pairs of nodes in a weighted graph. It also includes
a function for detecting negative cycles within a graph.

"""
import time
import numpy as np

def floyd_warshall_iterative(weights):
    """
    Iterative implementation of the Floyd-Warshall algorithm.
    """
    if weights.size == 0:
        # Immediately return for empty matrix
        return weights

    num_nodes = len(weights)

    dist = np.copy(weights)

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def floyd_warshall_recursive(weights, k=0):
    """
    Recursive implementation of the Floyd-Warshall algorithm.
    """
    if weights.size == 0:
        # Immediately return for empty matrix
        return weights

    num_nodes = len(weights)

    if k == num_nodes:
        # Base case: all intermediate nodes have been considered
        return weights

    # Update the distance matrix recursively
    def update_distances(i, j):
        if i == num_nodes:
            return  # Exit condition for the first loop
        if j == num_nodes:
            update_distances(i + 1, 0)  # Move to next row in the matrix
        else:
            if weights[i][k] != float('inf') and weights[k][j] != float('inf'):
                weights[i][j] = min(weights[i][j], weights[i][k] + weights[k][j])
            update_distances(i, j + 1)  # Continue to the next column

    update_distances(0, 0)  # Start updating distances

    # Recursive call with the next intermediate node
    return floyd_warshall_recursive(weights, k + 1)

def floyd_warshall_recursive_performance(weights):
    """
    Performance wrapper function for the Floyd Warshall Recursive implementation.
    """
    start_time = time.time()
    result = floyd_warshall_recursive(np.copy(weights))
    end_time = time.time()
    return result, end_time - start_time

def floyd_warshall_iterative_performance(weights):
    """
    Performance wrapper function for the Floyd Warshall Iterative implementation.
    """
    start_time = time.time()
    result = floyd_warshall_iterative(np.copy(weights))
    end_time = time.time()
    return result, end_time - start_time

def detect_negative_cycle(dist):
    """
    Detect if a negative cycle exists in the graph based on the distance matrix 
    from the Floyd-Warshall algorithm.
    
    :param dist: numpy array representing the shortest path distances between all pairs of nodes
    :return: boolean indicating the presence of a negative cycle
    """
    return np.any(dist.diagonal() < 0)
