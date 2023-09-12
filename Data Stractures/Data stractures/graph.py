import pydot
from random import randint
class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def remove_edge(self, v1, v2):
        self.graph[v1].remove(v2)
        self.graph[v2].remove(v1)

    def remove_vertex(self, v):
        while len(self.graph) > 0:
            edge = self.graph[v].pop()
            self.remove_edge(v, edge)
        del self.graph[v]
    def getStart(self):
        return list(self.graph.keys())[0]
    def DFS(self, v):
        result = []
        visited = {}

        if v not in self.graph:
                return None

        def dfs_helper(vertex):
            visited[vertex] = True
            result.append(vertex)

            for v in self.graph[vertex]:
                if v not in visited:
                    return dfs_helper(v)
        dfs_helper(v)
        return result

    def BFS(self, v):
        result = []
        visited = {}
        queue = [v]
        current_vertex = None

        visited[v] = True

        while len(queue) > 0:
            current_vertex = queue.pop(0)
            result.append(current_vertex)

            for v in self.graph[current_vertex]:
                if v not in visited:
                    visited[v] = True
                    queue.append(v)
        return result

def build_graph():

    map = Graph()

    for v in range(20):
        map.add_vertex(v)

    vertices = list(map.graph.keys())

    for v in range(len(vertices)):
        for i in range(v+1, v+3):
            map.add_edge(vertices[v], vertices[i%len(vertices)])
            

    # print(map.graph[0])
    # print(map.graph[map.getStart()])

    # print(map.DFS(0))
    # print(map.BFS(1))

    # plot map
    visulaize = pydot.Dot("graphdotfile")
    for key, value in map.graph.items():
        for v in value:
            visulaize.add_edge(pydot.Edge(key, v, label ="A"))

    visulaize.write_svg("graph.svg")
    # file = open("graphfile.gv", "w")
    # file.write(str(visulaize))
    return map

if __name__ == '__main__':
    map = Graph()
    

    for v in range(20):
        map.add_vertex(v)

    vertices = list(map.graph.keys())

    for v in range(len(vertices)):
        for i in range(v+1, v+3):
            map.add_edge(vertices[v], vertices[i%len(vertices)])
            

    print(map.graph[0])
    print(map.graph[map.getStart()])

    print(map.DFS(0))
    print(map.BFS(0))


    visulaize = pydot.Dot("graphdotfile")
    for key, value in map.graph.items():
        for v in value:
            visulaize.add_edge(pydot.Edge(key, v, label ="A"))

    visulaize.write_svg("graph.svg")
    # file = open("graphfile.gv", "w")
    # file.write(str(visulaize))


import pydot
from random import randint
class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2, cost):
        self.graph[v1].append({"vertice": v2, "cost": cost})
        # self.graph[v2].append({"vertice": v1, "cost": cost})

    def getStart(self):
        return list(self.graph.keys())[0]

    def dfs(self, v):
        result = []
        visited = {}

        if v not in self.graph:
            return None

        def dfs_helper(vertex):
            visited[vertex] = True
            result.append(vertex)

            for v in self.graph[vertex]:
                if v["vertice"] not in visited:
                    return dfs_helper(v["vertice"])
        dfs_helper(v)
        return result

    def bfs(self, v):
        result = []
        visited = {}
        queue = [v]
        current_vertex = None

        visited[v] = True

        while len(queue) > 0:
            current_vertex = queue.pop(0)
            result.append(current_vertex)

            for v in self.graph[current_vertex]:
                if v["vertice"] not in visited:
                    visited[v["vertice"]] = True
                    queue.append(v["vertice"])
        return result
    def get_exit(self):
        return list(self.graph.keys())[-1]


def build_graph():

    map = Graph()
    for v in range(20):
        map.add_vertex(v)

    vertices = list(map.graph.keys())

    for v in range(len(vertices)):
        for i in range(v+1, v+3):
            map.add_edge(vertices[v], vertices[i % len(vertices)], i)
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
    map = Graph()
    map.add_vertex("A")
    map.add_vertex("B")
    map.add_vertex("C")
    map.add_vertex("E")
    map.add_vertex("D")
    map.add_edge("A", "B", 6)
    map.add_edge("A", "C", 10)
    map.add_edge("A", "D", 4)

    map.add_edge("B", "C", 3)

    map.add_edge("C", "E", 8)

    map.add_edge("E", "B", 5)

    map.add_edge("E", "D", 7)

    map.add_edge("D", "C", 12)

    print(map.graph)

    # print(map.dfs('A'))
    # print(map.bfs("A"))


    # map = Graph()

    # for v in range(20):
    #     map.add_vertex(v)

    # vertices = list(map.graph.keys())

    # for v in range(len(vertices)):
    #     for i in range(v+1, v+3):
    #         map.add_edge(vertices[v], vertices[i % len(vertices)], i)

    # print(map.graph[0])
    # print(map.graph[1])
    # print(map.graph)
    # print(map.getStart())
    # print(map.graph[map.getStart()])

    # print(map.dfs(0))
    # print(map.bfs(0))
    # print(map.get_exit())

    # visulaize = pydot.Dot("graphdotfile")
    # for key, value in map.graph.items():
    #     for v in value:
    #         visulaize.add_edge(pydot.Edge(
    #             key, v["vertice"], label=str(v["cost"])))

    # visulaize.write_svg("graph.svg")
    # # file = open("graphfile.gv", "w")
    # # file.write(str(visulaize))
