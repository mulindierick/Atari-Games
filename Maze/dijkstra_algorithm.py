from priority_queue import PriorityQueue

def dijkstra(start, finish, map):
    
    priority = PriorityQueue()
    distances = {}
    previous = {}
    curr_path = None
    cheapest_path = []

    for vertex in map.keys():
        if vertex == start:
            distances[vertex] = 0
            priority.enqueue(vertex, 0)
        else:
            distances[vertex] = float("inf")
            priority.enqueue(vertex, float("inf"))
        previous[vertex] = None

    while (priority.priority_queue.min_heap_len()):

        curr_path = priority.dequeue()["node"]

        if (curr_path == finish):
            while (previous[curr_path] != None):
                cheapest_path.insert(0, curr_path)
                curr_path = previous[curr_path]
            break

        if (curr_path or distances[curr_path] != float("inf")):
            for neighbour in map[curr_path]:
                distance_to_neighbour = distances[curr_path] + \
                    neighbour["cost"]
                if (distance_to_neighbour < distances[neighbour["vertice"]]):
                    distances[neighbour["vertice"]] = distance_to_neighbour
                    previous[neighbour["vertice"]] = curr_path
                    priority.enqueue(
                        neighbour["vertice"], distance_to_neighbour)

    cheapest_path.insert(0, curr_path)
    return cheapest_path


if __name__ == '__main__':
    print(dijkstra(1, 17))
