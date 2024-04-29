"""
Test suite for the Algorithms module
"""
import unittest
import numpy as np
import algorithms as algo

class TestFloydWarshallAlgorithms(unittest.TestCase):
    """
    Unit tests for the Floyd-Warshall algorithm implementations and negative cycle detection.
    """
    def test_floyd_warshall_iterative(self):
        """Test the iterative implementation"""
        weights = np.array([
            [0, 3, np.inf],
            [np.inf, 0, 1],
            [4, np.inf, 0]
        ])
        expected = np.array([
            [0, 3, 4],
            [5, 0, 1],
            [4, 7, 0]
        ])
        result = algo.floyd_warshall_iterative(weights)
        np.testing.assert_array_equal(result, expected)

    def test_floyd_warshall_recursive(self):
        """Test the recursive implementation"""
        weights = np.array([
            [0, 3, np.inf],
            [np.inf, 0, 1],
            [4, np.inf, 0]
        ])
        expected = np.array([
            [0, 3, 4],
            [5, 0, 1],
            [4, 7, 0]
        ])
        result = algo.floyd_warshall_recursive(weights)
        np.testing.assert_array_equal(result, expected)

    def test_detect_negative_cycle(self):
        """Test the detection of negative cycles in the graph"""
        # Setting up a graph that definitely contains a negative cycle
        weights = np.array([
            [0, 1, np.inf],
            [np.inf, 0, -1],
            [-1, np.inf, 0]
        ])
        # Run the Floyd-Warshall algorithm to compute the shortest paths
        dist = algo.floyd_warshall_iterative(weights)
        # Check if the resulting distance matrix indicates a negative cycle
        self.assertTrue(algo.detect_negative_cycle(dist))

    def test_empty_graph(self):
        """Test an empty graph"""
        weights = np.array([[]])
        expected = np.array([[]])
        result = algo.floyd_warshall_iterative(weights)
        np.testing.assert_array_equal(result, expected)
        result = algo.floyd_warshall_recursive(weights)
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
