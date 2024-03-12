# Constraint Satisfaction Problem (CSP) - Graph Coloring

The program reads a graph and the number of colors in a text file and finds whether the graph is colorable with the given number of colors. The proper vertex coloring is such that each vertex is assigned a color and no two adjacent vertices are assigned the same color.

## Prerequisites

Before you run the code, ensure you have met the following requirements:


- Make sure to install python on your machine. Version used for this task is `3.11.5`.

## How to Run the Code

To run the code on your local machine, follow these steps:

 **Run the program**:
   In the root folder, run the below command:
   ```sh
   python graph_coloring_test.py
   ```
  
  After running this command you will get one of these two results:
  - **`Solution found`** if the graph is colorable with the given input, you will also see the assigned color of each vertex and whether it passed a simple unit test
  - **`Solution not found`** with the error otherwise

Feel free to change the input graph. It can be done by changing `graph_file = "tests/gc_78317103208800.txt"` to any other graph in `graph_coloring_test.py` file. I also added some ready graphs in the `tests` folder.

``` sh
Colors = 3
1,3 
2,18 
3,19 
2,19
```
The graph presented above has 5 vertices: “1”, “2”, “3”, “18” and “19”, and 4 edges.

***THANK YOU, HAVE FUN TESTING THE CODE :)***
