class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = []
        for i in range(size):
            self.adj_matrix.append([0 for i in range(self.size)])
    
    def add_edges(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d"% (v1,v2))
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
    
    def remove_edge(self, v1, v2):
        if self.adj_matrix[v1][v2] == 0:
            print("no edges between {v1} and {v2}")
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def len(self):
        return self.size * self.size
    
    def print_matrix(self):
        for row in self.adj_matrix:
            for val in row:
                print(val, end=" ")
            print()

def main():
    g = Graph(4)
    g.add_edges(0,1)
    g.add_edges(0,2)
    g.add_edges(0,3)
    g.add_edges(1,0)
    g.add_edges(1,2)
    g.add_edges(2,0)
    g.add_edges(2,1)
    g.add_edges(3,0)
    g.print_matrix()

if __name__ == "__main__":
    main()
