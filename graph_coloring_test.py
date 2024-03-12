import unittest
from graph_coloring_csp import GraphColoringCSP

class TestGraphColoringCSP(unittest.TestCase):
    def test_solve(self):
        # Test case to check if a solution is found for the given graph file

        # Specify the path to the graph file
        graph_file = "tests/gc_78317103208800.txt"

        # Create an instance of the GraphColoringCSP class with the specified graph file
        csp = GraphColoringCSP(graph_file)

        # Attempt to find a solution using the solve method
        solution = csp.solve()

        # Assert that a solution is found (not None), otherwise fail the test with a custom message
        self.assertIsNotNone(solution, "Solution not found")

# Run the test case if the script is executed directly
if __name__ == "__main__":
    unittest.main()
