import heapq

graph=[
    [0,6,2,0,0,0,10],
    [6,0,3,1,0,0,0],
    [2,3,0,0,6,2,0],
    [0,1,0,0,4,0,0],
    [0,0,6,4,0,3,0],
    [0,0,2,0,3,0,1],
    [10,0,0,0,0,1,0]
]

heuristic=[5,3,3,2,6,3,0]

start=0

goal=6
pq=[]

heapq.heappush(pq,(0+heuristic[start],0,start,str(start)))

visited=[False]*7

while pq:
    f,g,curr,path=heapq.heappop(pq)

    if curr== goal:
        print("Goal founded")
        print(f"path:  {path}")
        print(f"Cost is : {g}")
        break


    if visited[curr]:
        continue
    visited[curr]=True


    for i in range(len(graph)):
        weight=graph[curr][i]
        if weight!=0 and not visited[i]:
            new_g=g+weight
            new_f=new_g+heuristic[i]

            new_path=path+ '->'+str(i)

            heapq.heappush(pq,(new_f,new_g,i,new_path))