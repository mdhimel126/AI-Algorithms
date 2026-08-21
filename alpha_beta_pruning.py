import math

def minimax(current,nodeIndex,maxTurn,scores,treeDepth,alpha,beta):
    if current==treeDepth:
        return scores[nodeIndex]

    if maxTurn:
        best=-math.inf

        left=minimax(current+1,nodeIndex*2,False,scores,treeDepth,alpha,beta)

        best=max(best,left)

        alpha=max(alpha,best)

        if beta <= alpha:
            return best
        right=minimax(current+1,nodeIndex*2+1,False,scores,treeDepth,alpha,beta)

        best=max(best,right)

        alpha=max(alpha,best)

        return alpha

    else:
        best=math.inf

        left=minimax(current+1,nodeIndex*2,True,scores,treeDepth,alpha,beta)
        best=min(best,left)

        beta=min(best,beta)

        if beta <= alpha:
            return best

        right=minimax(current+1,nodeIndex*2+1,True,scores,treeDepth,alpha,beta)
        best=min(best,right)

        beta=min(best,beta)

        return beta
        


n=int(input("Enter no of  left nodes: "))

scores=[int(input()) for _ in range(n)]

treeDepth=math.log2(n)

result=minimax(0,0,True,scores,treeDepth,-math.inf,math.inf)

if result:
    print(f"The optimal anss is: {result}")
  