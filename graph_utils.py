import networkx as nx

def read_graph(graph_file):
    # Read the content of the specified graph file
    with open(graph_file, 'r') as file:
        lines = file.readlines()

    # Default value for the number of colors in case it's not specified in the file
    num_colors = 1

    # Iterate through each line in the file to find the number of colors
    for line in lines:
        line = line.strip()

        # Skip comments
        if line.startswith('#'):
            continue

        # Check if the line contains information about the number of colors
        if "colors" in line:
            # Extract the number of colors from the line
            num_colors = int(line.split('=')[1])
            break  # Stop searching after finding the colors line

    # Extract edges from the lines, ignoring comments, and create a graph
    edges = [tuple(map(int, line.strip().split(','))) for line in lines if ',' in line and not line.startswith('#')]
    G = nx.Graph()
    G.add_edges_from(edges)

    # Return the created graph and the number of colors
    return G, num_colors
