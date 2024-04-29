#!/usr/bin/env python3
"""
Test suite for validating the utility functions.
"""
import unittest
import numpy as np
import matplotlib.pyplot as plt
from ..utils import generate_random_graph, plot_performance

class TestGenerateRandomGraph(unittest.TestCase):
    """
    Test the generation of random matricies
    """
    def test_matrix_shape(self):
        """Test if the output matrix has the correct shape."""
        num_nodes = 5
        graph = generate_random_graph(num_nodes)
        self.assertEqual(graph.shape, (num_nodes, num_nodes))

    def test_negative_weights(self):
        """Test if negative weights are included when specified."""
        num_nodes = 5
        graph = generate_random_graph(num_nodes, allow_negative=True)
        self.assertTrue(np.any(graph < 0))

    def test_no_negative_weights(self):
        """Test that no negative weights are included by default."""
        num_nodes = 5
        graph = generate_random_graph(num_nodes)
        self.assertTrue(np.all(graph >= 0))

    def test_zero_nodes(self):
        """Test the output for zero nodes."""
        graph = generate_random_graph(0)
        self.assertEqual(graph.size, 0)

class TestPlotPerformance(unittest.TestCase):
    """
    Test the generation of the matplotlib graph
    """
    def test_plot_output(self):
        """Test if the function returns a matplotlib figure object."""
        data = {
            'sizes': [10, 20, 30],
            'iterative_times': [1, 2, 3],
            'recursive_times': [3, 2, 1]
        }
        fig = plot_performance(data)
        self.assertIsInstance(fig, plt.Figure)

    def test_plot_elements(self):
        """Test if the plot includes necessary elements."""
        data = {
            'sizes': [10, 20, 30],
            'iterative_times': [1, 2, 3],
            'recursive_times': [3, 2, 1]
        }
        fig = plot_performance(data)
        ax = fig.axes[0]
        self.assertTrue(any('Iterative' in str(leg) for leg in ax.get_legend().get_texts()))
        self.assertTrue(any('Recursive' in str(leg) for leg in ax.get_legend().get_texts()))
        self.assertEqual(ax.get_xlabel(), 'Number of Nodes')
        self.assertEqual(ax.get_ylabel(), 'Execution Time (seconds)')
        self.assertEqual(ax.get_title(), 'Performance Comparison: Iterative vs. Recursive')
