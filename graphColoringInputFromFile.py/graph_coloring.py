class Graph_color():
    def __init__(self):
        self.V=0
        self.C=0
        self.color=[]
        self.graph=[]

    def graph_color(self,graph,c):
        self.V=len(graph)
        self.C=c
        self.color=[0]* self.V
        self.graph=graph

        if not self.solve(0):
            return False
        return True

    def solve(self,v):
        if v==self.V:
            return True

        for c in range (1,self.C+1):
            if self.is_possible(v,c):
                self.color[v]=c

                if self.solve(v+1):
                    return True
                self.color[v]=0

        return False

    def is_possible(self,v,c):
        for i in range(self.V):
            if self.graph[v][i]==1 and self.color[i]==c:
                return False

        return True    

with open("graphColoringInputFromFile.py/input.txt","r") as f:
    N,M,K=map(int,f.readline().split())

    graph=[[0]* N for _ in range(N)]

    for _ in range(M):
        u,v=map(int,f.readline().split())

        graph[u][v]=1
        graph[v][u]=1

gc=Graph_color()

if gc.graph_color(graph,K):
    print(f"Coloring possible with {K} colors")       
    print(f"Color assignment: {gc.color}")

else:
    print(f"Coloring not possible with {K} colors")








