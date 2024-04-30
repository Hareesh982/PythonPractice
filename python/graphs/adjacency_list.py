
class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None
class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V
    
    def add_edges(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node
    def print_graph(self):
        for i in range(self.V):
            print("vertex " + str(i) + ":",end="" )
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}",end = " ")
                temp = temp.next
            print()
def main():
    V = 4
    g = Graph(V)
    g.add_edges(0,1)
    g.add_edges(0,2)
    g.add_edges(0,3)
    g.add_edges(1,2)
    g.print_graph()

if __name__ == "__main__":
    main()