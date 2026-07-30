class GraphColor:
    def __init__(self):
        self.V=0
        self.C=0
        self.color=[]
        self.graph=[]

    def graphColor(self,graph,c):
        self.V=0
        self.C=c
        self.color=[0] *self.V
        self.graph=graph

        try:
            self.solve(0)
            print("No solution")
        except Exception as e:
            print("Solution exists")

    def solve(self,v):
        if v==self.V:
            raise Exception("solution found")

        for i in range(1,self.C+1):
            if self.isPossible(v,i):
                self.color[v]=i
                self.solve(v+1)  
                self.color[v]=0

    def isPossible(self,v,c):
        for i in range(self.V):
            if self.graph[v][i]==1 and self.color[i]==c:
                return False
        return True


V=int(input("No of V:"))
c=int (input("No of c:"))
graph=[]

for i in range(V):
    row=list(map(int,input().split()))
    graph.append(row)

gc=GraphColor()
gc.graphColor(graph,c)    




        


