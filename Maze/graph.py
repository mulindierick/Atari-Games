import pydot
from random import randint
from queue_ds import Queue


class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2, cost):
        self.graph[v1].append({"vertice": v2, "cost": cost})
        self.graph[v2].append({"vertice": v1, "cost": cost})

    def getStart(self):
        return list(self.graph.keys())[randint(1, 40)]

    def dfs(self, v, data):
        result = []
        visited = {}

        if v not in self.graph:
            return None

        def dfs_helper(vertex):
            visited[vertex] = True
            result.append(vertex)
            if (vertex == data):
                return result

            for v in self.graph[vertex]:
                if v["vertice"] not in visited:
                    return dfs_helper(v["vertice"])

        return dfs_helper(v)

    def bfs(self, v, data):
        result = []
        visited = {}
        queue = Queue()
        queue.enqueue(v)
        current_vertex = None
        visited[v] = True

        while queue.length > 0:
            current_vertex = queue.dequeue()
            result.append(current_vertex)
            if (current_vertex == data):
                return result

            for v in self.graph[current_vertex]:
                if v["vertice"] not in visited:
                    visited[v["vertice"]] = True
                    queue.enqueue(v["vertice"])
        return None

    def get_exit(self):
        return list(self.graph.keys())[-1]


def build_graph():

    map = Graph()
    for v in range(0, 100):
        map.add_vertex(randint(0, 100))

    vertices = list(map.graph.keys())

    for v in range(len(vertices)):
        for i in range(v+1, v+3):
            map.add_edge(vertices[v], vertices[i %
                         len(vertices)], randint(0, 100))
    return map


def get_map():

    # plot map
    map = build_graph()
    visulaize = pydot.Dot("graphdotfile")
    for key, value in map.graph.items():
        for v in value:
            visulaize.add_edge(pydot.Edge(
                key, v["vertice"], label=str(v["cost"])))

    visulaize.write_svg("graph.svg")


if __name__ == '__main__':
    pass
    map = Graph()

    for v in range(100):
        map.add_vertex(randint(0, 100))

    vertices = list(map.graph.keys())

    for v in range(len(vertices)):
        for i in range(v+1, v+3):
            map.add_edge(vertices[v], vertices[i %
                         len(vertices)], randint(0, 100))

    print(map.graph[map.getStart()])
    print(map.graph[map.getStart()])
    # print(map.graph)
    print(map.getStart())
    print(map.graph[map.getStart()])

    print(map.dfs(map.getStart(), map.get_exit()))
    print(map.bfs(map.getStart(), map.get_exit()))
    print(map.get_exit())

    visulaize = pydot.Dot("graphdotfile")
    for key, value in map.graph.items():
        for v in value:
            visulaize.add_edge(pydot.Edge(
                key, v["vertice"], label=str(v["cost"])))

    visulaize.write_svg("graph.svg")
    # file = open("graphfile.gv", "w")
    # file.write(str(visulaize))

    print("wwjw", len(list(map.graph.keys())))
