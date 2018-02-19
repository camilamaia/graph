Graph - Dijkstra's Algorithm Implementation
=====

A implementation of Dijkstra's algorithm for finding the shortest paths between nodes in a given graph.

Software developed for the Graph Class INE5413, of the Department of Informatics and Statistics of the Federal University of Santa Catariana in the second semester of 2013.

-----

## How to Run

Inside the project directory, run: 

```bash
    $ ./bin/graph
```

By default, the script uses the graph below to calculate the shortest paths between nodes:

```python
    {
       A {'B': 7, 'G': 3, 'F': 5}
       C {'B': 2, 'E': 3, 'D': 5, 'G': 2}
       B {'A': 7, 'C': 2, 'G': 3}
       E {'C': 3, 'D': 4, 'G': 4, 'F': 6}
       D {'C': 5, 'E': 4}
       G {'A': 3, 'C': 2, 'B': 3, 'E': 4, 'F': 3}
       F {'A': 5, 'E': 6, 'G': 3}
    }
```

If you want to provide your own graph, run the script with the `Create your own graph` option:

```bash
    $ ./bin/graph -c
```
