def dfs(grid,start,goal):
    n=len(grid)
    steps=[(1,0),(-1,0),(0,1),(0,-1)]
    stack=[(start[0],start[1],0)]
    grid[start[0]][start[1]]=0

    while stack:
        x,y,moves=stack.pop()

        if (x,y)== goal:
            return True,moves

        for dx,dy in steps:
            nx=x+dx
            ny=y+dy

            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1:
                stack.append((nx,ny,moves+1))
                grid[nx][ny]=0
    return False,None            




grid=[
    [0,1,0,1,1],
    [0,1,1,1,0],
    [0,1,0,0,1],
    [0,1,1,0,1],
    [0,0,1,1,1]
]

start=(0,3)
goal=(4,3)

found,moves=dfs(grid,start,goal)

if found:
    print(f"Solution Found in {moves} moves")
else:
    print("Solution not found")    