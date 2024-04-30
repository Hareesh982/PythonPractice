from collections import defaultdict 

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 

    def add_edge(self,u,v): 
        self.graph[u].append(v) 

    def DFSUtil(self, v, visited): 
        visited.add(v) 
        print(v, end=' ') 

        for i in self.graph[v]: 
            if i not in visited: 
                self.DFSUtil(i, visited) 

    def DFS(self, v): 
        visited = set() 
        self.DFSUtil(v, visited) 

if __name__ == "__main__":
    g = Graph() 
    g.add_edge(0, 1) 
    g.add_edge(0, 2) 
    g.add_edge(1, 2) 
    g.add_edge(2, 0) 
    g.add_edge(2, 3) 
    g.add_edge(3, 3) 

    print ("Following is Depth First Traversal (starting from vertex 2)") 
    g.DFS(2) 
