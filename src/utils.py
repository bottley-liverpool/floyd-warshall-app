#!/usr/bin/env python3
"""
Utility functions for the Floyd-Warshall Algorithm Streamlit app.

This module provides helper functions used throughout the application.
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_random_graph(num_nodes, allow_negative=False, max_weight=10):
    """
    Generate a random adjacency matrix for a graph with a specified number of nodes.
    Optionally allow negative weights for edges.

    :param num_nodes: int number of nodes in the graph
    :param allow_negative: bool whether to include negative weights
    :param max_weight: int maximum number of nodes
    
    :return: numpy array representing the adjacency matrix of the graph
    """
    graph = np.random.randint(1, max_weight, size=(num_nodes, num_nodes))
    if allow_negative:
        neg_modifier = np.random.choice([1, -1], size=(num_nodes, num_nodes), p=[0.8, 0.2])
        graph = graph * neg_modifier
    np.fill_diagonal(graph, 0)
    return graph

def plot_performance(data):
    """
    Plot the performance data using Matplotlib.

    :param data: dict performance data
    :return: matplotlib figure object containing the plotted performance comparison.
    """
    fig, ax = plt.subplots()
    ax.plot(data['sizes'], data['iterative_times'], label='Iterative', marker='o')
    ax.plot(data['sizes'], data['recursive_times'], label='Recursive', marker='x')
    ax.set_xlabel('Number of Nodes')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Performance Comparison: Iterative vs. Recursive')
    ax.legend()
    return fig
