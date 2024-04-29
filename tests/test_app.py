"""
Test suite for validating the functionality of the Streamlit application.
"""
import unittest
from streamlit.testing.v1 import AppTest

class TestStreamlitApp(unittest.TestCase):
    """
    Test the application's response to mode selection and execution 
    in the streamlit application.
    """

    def setUp(self):
        """Initialize AppTest and run the Streamlit app."""
        self.at = AppTest.from_file("app.py")
        self.at.run()

    def test_mode_selection_demo(self):
        """Test mode selection and functionality in Demo mode."""
        self.at.selectbox("mode_select").select("Demo").run()
        self.at.button("run_algorithm").click().run()
        # Check if the graph matrix is displayed using the appropriate output method
        self.assertTrue(
            any("Resulting Distance Matrix:" in elem.value for elem in self.at.markdown)
        )

    def test_negative_cycle_detection(self):
        """Test negative cycle detection functionality."""
        self.at.selectbox("mode_select").select("Negative Cycle Detection").run()
        self.at.checkbox("allow_negative_weights").check().run()

        # Load a random graph
        self.at.button("generate_random_graph").click().run()

        # Click the button by its key
        self.at.button("run_algorithm").click().run()

        assert self.at.error[0].value == "A negative cycle has been detected in the graph."

    def test_performance_testing(self):
        """Test the performace testing functionality"""
        self.at.selectbox("mode_select").select("Performance Testing").run()

        self.at.slider("number_nodes").set_value(20).run()

        # Load the graph
        self.at.button("generate_performance_test").click().run()

        assert self.at.success[0].value == "Performance test completed successfully for 20 nodes!"

if __name__ == '__main__':
    unittest.main()
