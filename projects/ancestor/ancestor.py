

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.vertices[v1].add(v2)

    def get_ancestor(self, vertex_id):
        return self.vertices[vertex_id]
    
    def bfs(self, starting_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        longest_path_length = 1
        earliest_ancestor = -1

        while queue.size() > 0:
            path_to_current_node = queue.dequeue()
            current_node = path_to_current_node[-1]

            if len(path_to_current_node) > longest_path_length or \
                    ((len(path_to_current_node) == longest_path_length and current_node < earliest_ancestor)):
                longest_path_length = len(path_to_current_node)
                earliest_ancestor = current_node

            for ancestor in self.get_ancestor(current_node):
                path_to_ancestor = [*path_to_current_node, ancestor]
                queue.enqueue(path_to_ancestor)

        return earliest_ancestor


def bfs(self, starting_vertex):
    queue = Queue()
    queue.enqueue([starting_vertex])
    longest_path_length = 1
    earliest_ancestor = -1

    while queue.size() > 0:
        path_to_current_node = queue.dequeue()
        current_node = path_to_current_node[-1]

        if len(path_to_current_node) > longest_path_length or \
                ((len(path_to_current_node) == longest_path_length and current_node < earliest_ancestor)):
            longest_path_length = len(path_to_current_node)
            earliest_ancestor = current_node

        for ancestor in self.get_ancestor(current_node):
            path_to_ancestor = [*path_to_current_node, ancestor]
            queue.enqueue(path_to_ancestor)

    return earliest_ancestor


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])
    return graph.bfs(starting_node)
