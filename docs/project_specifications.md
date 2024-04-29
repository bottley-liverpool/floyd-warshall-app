### Specification Document for Floyd-Warshall Algorithm App

#### Overview
The Streamlit application is designed to demonstrate the functionality of the Floyd-Warshall algorithm, focusing on calculating the shortest paths between nodes in a graph and detecting negative cycles. It includes the following features 
- Basic demonstration of the algorithm for both the iterative and recursive implementation
- The ability to detect negative cycles in a provided graph
- Performance comparisons between iterative and recursive implementations of the algorithm.

#### Functional Requirements
1. **Graph Generation**
   - The application must allow users to generate random graphs with a specified number of nodes.
   - Users should be able to toggle the inclusion of negative weights in the graph.

2. **Algorithm Demonstration**
   - The app must provide options to:
     - Calculate the shortest paths between all pairs of nodes using the Floyd-Warshall algorithm.
     - Detect negative cycles within the graph.
   - Each implementaton should have a button to execute the respective algorithm.

3. **Mode Selection**
   - Users should be able to select between different modes:
     - Basic demonstration of the algorithm.
     - Negative cycle detection.
     - Performance testing (comparing iterative and recursive implementations).

4. **Display Results**
   - The application must display the adjacency matrix of the graph and the results matrix after algorithm execution.
   - For negative cycle detection, the app should indicate whether a negative cycle was detected.

5. **Performance Testing**
   - The app should allow users to execute both iterative and recursive implementations of the Floyd-Warshall algorithm and display the execution time for each.

#### Non-Functional Requirements
1. **Usability**
   - The app should be user-friendly with clear labels for all inputs and buttons.
   - Results should be presented in a readable format that clearly distinguishes between different types of outputs.

2. **Performance**
   - The application should perform calculations within a reasonable time frame, ensuring that algorithm execution does not exceed 3 seconds for graphs up to 25 nodes in a typical use case.
   - The app should handle up to 25 nodes efficiently in the web interface without degradation in responsiveness.

3. **Reliability**
   - The application should provide consistent results across different executions and environments.

4. **Maintainability**
   - The code should be well-documented and structured to facilitate easy updates and maintenance.
   - The application should use modular architecture where core functionalities like graph generation and the Floyd-Warshall algorithm are isolated from the UI code.

5. **Accessibility**
   - Basic accessibility features such as keyboard navigability and readable fonts should be implemented.