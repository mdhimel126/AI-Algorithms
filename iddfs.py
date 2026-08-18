def dls(graph,curr,goal,depth,lim,visited,path):
    if curr==goal:
        return True,path

    if depth>=lim:
        return False,path

    for n in range(len(graph[curr])):
        if graph[curr][n]==1 and n not in visited:
            visited.add(n)

            found,final_path= dls(graph,n,goal,depth+1,lim,visited,path+[n])
            if found:
                return True,final_path
            visited.remove(n)
    return False,path        



def iddfs(graph,start,goal,max_limit=20):

    for lim in range(max_limit+1):
        visited={start}

        found,path= dls(graph,start,goal,0,lim,visited,[start])
        if found:
            return path
    return False    



graph=[
    [0,1,1,0,0,0,0],
    [0,0,0,1,1,0,0],
    [0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

start=int(input("Enter start node: "))
goal=int(input("Enter goal node: "))

path=iddfs(graph,start,goal,max_limit=10)

if path:
    print("Solution exists")
    print("The path is : ",end=" ")
    for p in path:
        print(f"->{p}",end=" ")
else:
    print("Solution doesn't exists")    
