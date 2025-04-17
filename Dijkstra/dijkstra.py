class Edge:
    def __init__(self, edge: tuple[int], weight: int):
        source ,dest = edge
        self.source = source
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self, edges: list[tuple[tuple[int],int]] =  None):
        self.nodes = []
        self.edges = []
        if edges is not None:
            self.add_edges(edges)

    def add_node(self, node: int):
            self.nodes.append(node)

    def add_edges(self, edges: list[tuple[tuple[int],int]]):
        for source_dest,w in edges:
            self.add_edge(source_dest,w)

    def add_edge(self, edge: tuple[int], weight: int):
        source, dest = edge
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        new_edge = Edge(edge, weight)
        self.edges.append(new_edge)

    def get_neighbors(self, node: int) -> list[int]:
        neighbors = []
        for edge in self.edges:
            if edge.source == node:
                neighbors.append(edge.dest)
        return neighbors

    def get_dist(self,node1,node2) -> int:
        for e in self.edges:
            if e.source == node1 and e.dest == node2:
                return e.weight
            if e.source == node2 and e.dest == node1:
                return e.weight
        raise Exception


    def compute_shortest_path(self, source: int, dest: int) -> list[int]:
        q =  set()
        dist = {}
        pred =  {}

        for node in self.nodes:
            dist[node] = float('inf')
            q.add(node)

        dist[source] = 0
        while q:
            u =  min(q)
            q.remove(u)
            neighbors =  self.get_neighbors(u)

            for n in neighbors:
                new = dist[u] + self.get_dist(u,n)
                if new < dist[n]:
                    dist[n] = new
                    pred[n] = u
        currNode = dest
        res = [currNode]
        while currNode != source:
            currNode =  pred[currNode]
            res.append(currNode)
        res.reverse()
        return res



if __name__ == "__main__":
    edgelist = [((0, 2), 4),
            ((0, 1), 2),
            ((1, 3), 3),
            ((2,4),2),
            ((4, 5), 2),
            ((3,5),4)
            ]
    g = Graph(edgelist)
    print(g.compute_shortest_path(0,5))
