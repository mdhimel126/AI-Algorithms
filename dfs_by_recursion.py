def dfs(grid,current,goal,path):
    x,y=current

    if (x,y)==goal:
        return True,path

    n=len(grid)
    moves=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    grid[x][y]=0

    for dx,dy in moves:
        nx=x+dx
        ny=y+dy

        if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
               found,final_path=dfs(grid,(nx,ny),goal,path+[(nx,ny)])
               if found:
                   return True,final_path
    return False,None       



grid = [ 
    [0,0,1,0,1,1], 
    [0,1,0,1,1,0], 
    [0,1,0,1,0,1],
    [1,1,0,1,1,0], 
    [0,0,1,0,0,1], 
    [0,1,0,0,1,1] 
] 

start=(0,2)
goal=(5,1)

found,path= dfs(grid,start,goal,[start])

if found:
    print("Solution found")
    print("And the path is:",end=" ")
    for i in path:
        print(i,end="->")

else:
    print("Sorry solution doesn't exists")    