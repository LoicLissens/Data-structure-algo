This algorithm was developped by Dijkstra to compute to shortest path between a node Na and Nb in a graph.
In our case the graph will be a weighted graph : this means on every link between to nodes we'll have a number that will be the weight of the link.

The weight can have different meaning regarding the use case eg:
- for a network linking router the weight could be the number of ms between each node.
- for google map it can be the travel time betweent those nodes.

the complexity is  `O(|E| + |V|*|V|)` where `|E|` is the number of edges and `V`the number of nodes