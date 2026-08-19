




import math

def minimax(scores,currDepth,nodeIndex,maxTurn,targetDepth):
    if currDepth==targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(scores,currDepth+1,nodeIndex*2,False,targetDepth),
            minimax(scores,currDepth+1,nodeIndex*2+1,False,targetDepth)
            )

    else:
        return min(
            minimax(scores,currDepth+1,nodeIndex*2,True,targetDepth),
            minimax(scores,currDepth+1,nodeIndex*2+1,True,targetDepth)
            )

n=int(input("Enter no of leaf node: "))
scores=[int(input(f"Score for leaf {i} :")) for i in range(n)]
treeDepth=math.log2(n)

print(f"The optimal value is :{minimax(scores,0,0,True,treeDepth)}")