#!/usr/bin/env python3
"""
Streamlit Application for Demonstrating the Floyd-Warshall Algorithm.
"""
import numpy as np
import streamlit as st
from algorithms import floyd_warshall_iterative_performance, floyd_warshall_recursive_performance, detect_negative_cycle
from utils import generate_random_graph, plot_performance

def main():
    """
    Sets up and runs the Streamlit UI components for demonstrating the Floyd-Warshall algorithm.
    Provides interactive controls for selecting demonstration mode, generating graphs,
    executing algorithms, and viewing results.
    """

    # Initialise the session state
    if 'graph' not in st.session_state:
        st.session_state['graph'] = None
    if 'performance_data' not in st.session_state:
        st.session_state['performance_data'] = None

    st.title("Floyd-Warshall Algorithm")

    # Sidebar configuration
    st.sidebar.header("Settings")
    mode = st.sidebar.selectbox(
        "Choose Mode", ["Demo", "Negative Cycle Detection", "Performance Testing"],
        key='mode_select'
        )
    num_nodes = st.sidebar.slider('Number of Nodes', 3, 20, 5, key='number_nodes')

    allow_negative = False
    if mode == "Negative Cycle Detection":
        allow_negative = st.sidebar.checkbox('Allow Negative Weights', value=False,
                                             key="allow_negative_weights")

    implementation = "Iterative"
    if mode != "Performance Testing":
        implementation = st.sidebar.selectbox("Implementation", ["Iterative", "Recursive"])

    # Manage graph generation and processing
    if mode != "Performance Testing":
        graph = None
        if mode == "Demo":
            graph = np.array([
                [0, 3, 8, float('inf'), -4],
                [float('inf'), 0, float('inf'), 1, 7],
                [float('inf'), 4, 0, float('inf'), float('inf')],
                [2, float('inf'), -5, 0, float('inf')],
                [float('inf'), float('inf'), float('inf'), 6, 0]
            ])
            st.session_state.graph = graph
            st.write("Example Graph (Adjacency Matrix):", graph)

        if mode != "Demo" and st.button('Generate Random Graph', key="generate_random_graph"):
            graph = generate_random_graph(num_nodes, allow_negative)
            st.session_state.graph = graph

        if mode != "Demo" and st.session_state.graph is not None:
            st.write("Graph (Adjacency Matrix):", st.session_state.graph)

        if st.button('Run Algorithm', key="run_algorithm"):
            if implementation == "Iterative":
                result, duration = floyd_warshall_iterative_performance(st.session_state.graph)
            else:
                result, duration = floyd_warshall_recursive_performance(st.session_state.graph)
            st.write("Resulting Distance Matrix:", result)
            st.write(f"{implementation} Execution Time: {duration:.6f} seconds")

            if mode == "Negative Cycle Detection":
                if detect_negative_cycle(result):
                    st.error("A negative cycle has been detected in the graph.")
                else:
                    st.success("No negative cycles detected.")

    # Performance testing mode
    if mode == "Performance Testing":
        if st.button('Generate and Test Implementations', key="generate_performance_test"):
            perform_performance_testing(num_nodes)
            st.success(f"Performance test completed successfully for {num_nodes} nodes!")

def perform_performance_testing(num_nodes):
    """
    Performs performance testing between iterative and recursive implementations 
    across different graph sizes.
    """
    iterative_times, recursive_times, sizes = [], [], range(3, num_nodes + 1)
    for size in sizes:
        graph = generate_random_graph(size)
        _, it_time = floyd_warshall_iterative_performance(graph)
        _, rec_time = floyd_warshall_recursive_performance(graph)
        iterative_times.append(it_time)
        recursive_times.append(rec_time)

    performance_data = {
        'sizes': list(sizes), 
        'iterative_times': iterative_times, 
        'recursive_times': recursive_times
    }
    st.session_state.performance_data = performance_data
    st.pyplot(plot_performance(st.session_state.performance_data))

if __name__ == "__main__":
    main()
