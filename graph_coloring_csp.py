import networkx as nx
from collections import deque
from graph_utils import read_graph

class GraphColoringCSP:
    def __init__(self, graph_file):
        # Initialize the GraphColoringCSP instance by reading the graph from the file
        # and extracting the number of colors from the file
        self.graph, self.colors = read_graph(graph_file)

    def is_valid_assignment(self, node, color, assignment):
        # Check if assigning 'color' to 'node' violates any constraints with neighbors
        for neighbor in self.graph.neighbors(node):
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def select_unassigned_variable(self, assignment):
        # Heuristic: Select the variable (node) with the fewest remaining values (neighbors)
        unassigned_nodes = [node for node in self.graph.nodes if node not in assignment]
        return min(unassigned_nodes, key=lambda v: len(list(self.graph.neighbors(v))))

    def order_domain_values(self, node, assignment):
        # Heuristic: Order domain values based on least constraining value (minimize impact on neighbors)
        colors = list(range(1, self.colors + 1))
        return sorted(colors, key=lambda c: sum(1 for neighbor in self.graph.neighbors(node) if neighbor not in assignment or assignment[neighbor] != c))

    def ac3(self, queue):
        # Constraint propagation using AC3 algorithm
        while queue:
            (xi, xj) = queue.popleft()
            if self.revise(xi, xj):
                if not list(self.graph.neighbors(xi)):
                    return False
                for xk in self.graph.neighbors(xi):
                    queue.append((xk, xi))
        return True

    def revise(self, xi, xj):
        # AC3: Remove inconsistent values from the domain of xi
        revised = False
        for color in range(1, self.colors + 1):
            if all(self.is_valid_assignment(xi, color, {xi: color, xj: c}) for c in range(1, self.colors + 1) if c != color):
                continue
            self.graph.remove_edge(xi, xj)
            revised = True
        return revised

    def backtracking_search(self):
        # Wrapper function to initiate the recursive backtracking search
        return self.backtrack({})

    def backtrack(self, assignment):
        # Recursive backtracking search with heuristics and constraint propagation
        if len(assignment) == len(self.graph.nodes):
            self.print_solution(assignment)
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_valid_assignment(var, value, assignment):
                assignment[var] = value
                if self.ac3(deque([(var, neighbor) for neighbor in self.graph.neighbors(var)])):
                    result = self.backtrack(assignment)
                    if result is not None:
                        return result
                del assignment[var]

        return None

    def print_solution(self, assignment):
        # Print the found solution with assigned colors for each node
        print("Solution found:")
        for node in sorted(assignment.keys()):
            print(f"Node {node}: Color {assignment[node]}")

    def solve(self):
        # Attempt to solve the CSP with the specified number of colors
        print("Trying with", self.colors, "colors")
        solution = self.backtracking_search()
        if solution is not None:
            return solution
        else:
            print("Solution not found.")
            return None
