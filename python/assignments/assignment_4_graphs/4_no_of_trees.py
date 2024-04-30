from collections import defaultdict 

class Graph: 
    def __init__(self, vertices): 
        self.graph = defaultdict(list) 
        self.vertices = vertices 

    def add_edge(self,u,v): 
        self.graph[u].append(v) 

    def dfs(self, visited, u): 
        visited[u] = True
        for i in self.graph[u]: 
            if visited[i] == False: 
                self.dfs(visited, i) 

    def count_trees(self): 
        visited = [False] * (self.vertices) 
        count = 0
        for i in range(self.vertices): 
            if visited[i] == False: 
                self.dfs(visited, i) 
                count += 1
        return count

if __name__ == "__main__":
    g = Graph(5) 
    g.add_edge(0, 1) 
    g.add_edge(0, 2) 
    g.add_edge(3, 4) 

    print("Number of trees in the forest:", g.count_trees()) 
