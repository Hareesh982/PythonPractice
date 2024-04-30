from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.visited = [False] * self.vertices
        self.rec_stack = [False] * self.vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, u):
        self.visited[u] = True
        self.rec_stack[u] = True

        for v in self.graph[u]:
            if not self.visited[v]:
                if self.is_cyclic_util(v):
                    return True
            elif self.rec_stack[v]:
                return True

        self.rec_stack[u] = False
        return False

    def is_cyclic(self):
        for u in range(self.vertices):
            if not self.visited[u]:
                if self.is_cyclic_util(u):
                    return True
        return False

if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    if g.is_cyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle")
