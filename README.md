### Floyd-Warshall Algorithm App

#### Overview
This Streamlit application demonstrates the Floyd-Warshall algorithm, focusing on comparing the performance between the iterative and recursive implementations. The application offers a simple user interface to interact with the algorithm's features, including:

- **Basic demonstration**: Visualizing the algorithm using both iterative and recursive implementations.
- **Negative cycle detection**: Checking graphs for the presence of negative cycles.
- **Performance testing**: Comparing execution times between the iterative and recursive approaches.

#### Features
- Generate random graphs with customizable settings.
- Select between different demonstration modes.
- Visual display of the adjacency matrix and the result matrix.
- Indicators for the presence of negative cycles.
- Performance metrics for algorithm executions.

#### Functional Requirements
- **Graph Generation**: Ability to generate graphs with a specified node count and optionally include negative weights.
- **Algorithm Demonstration**: Options to calculate shortest paths and detect negative cycles.
- **Mode Selection**: Users can choose from basic demonstration, negative cycle detection, and performance testing modes.
- **Display Results**: Visual outputs for adjacency matrices and result matrices along with cycle detection results.
- **Performance Testing**: Comparative execution times are displayed for iterative vs. recursive implementations.

### Demo Streamlit App
You can test the demo app at this url: [https://floyd-warshall-app.streamlit.app/](https://floyd-warshall-app.streamlit.app/)

#### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

##### Prerequisites
- Python 3.7 or higher
- Streamlit
- Matplotlib
- Numpy

##### Installation
1. Clone the repository:
```bash
git clone https://github.com/bottley-liverpool/floyd-warshall-app.git
```
2. Navigate to the project directory:
```bash
cd floyd-warshall-app
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

##### Running the Application
1. Navigate to the src directory:
```bash
cd src
```
2. Run the application using Streamlit:
```bash
streamlit run app.py
```

##### Running the Unit Tests
1. Navigate to the tests directory:
```bash
cd tests
```
Run the unit tests using Unittest:
```bash
python -m unittest
```

#### Usage
- **Mode Selection**: Use the sidebar to select between different modes (Basic, Negative Cycle Detection, Performance Testing).
- **Graph Settings**: Adjust the number of nodes and toggle negative weights as needed.
- **View Results**: Interact with the buttons to generate graphs and run algorithms. Results will be displayed on the main panel.

#### Authors
- **Brad Ottley** - *For the University of Liverpool* - [bottley-liverpool](https://github.com/bottley-liverpool)

#### License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/bottley-liverpool/floyd-warshall-app/docs/LICENSE.md) file for details