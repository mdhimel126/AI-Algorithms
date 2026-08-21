import math
import random

minmax_count=0
pruning_count=0

def minimax(current,nodeIndex,maxTurn,scores,treeDepth):
    global minmax_count
    minmax_count+=1

    if current==treeDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minimax(current+1,nodeIndex*2,False,scores,treeDepth),
                   minimax(current+1,nodeIndex*2+1,False,scores,treeDepth)
                   )

    else:
        return min(minimax(current+1,nodeIndex*2,True,scores,treeDepth),
                    minimax(current+1,nodeIndex*2+1,True,scores,treeDepth)
                    )


def alpha_beta_pruning(current,nodeIndex,maxTurn,scores,treeDepth,alpha,beta):
    global pruning_count
    pruning_count+=1

    if current==treeDepth:
        return scores[nodeIndex]

    if maxTurn:
        best=-math.inf

        left=alpha_beta_pruning(current+1,nodeIndex*2,False,scores,treeDepth,alpha,beta)
        best=max(best,left)

        alpha=max(alpha,best)

        if beta <= alpha:
            return best
        right=alpha_beta_pruning(current+1,nodeIndex*2+1,False,scores,treeDepth,alpha,beta)

        best=max(best,right)

        alpha=max(alpha,best)

        return best

    else:
        best=math.inf
        left=alpha_beta_pruning(current+1,nodeIndex*2,True,scores,treeDepth,alpha,beta)

        best=min(best,left)

        beta=min(beta,best)

        if beta <= alpha:
            return best

        right=alpha_beta_pruning(current+1,nodeIndex*2+1,True,scores,treeDepth,alpha,beta)

        best=min(best,right)
        beta=min(beta,best)
        return best
        


n=random.choice([8,16])

scores=[random.randint(1,30) for _ in range(n)]

treeDepth=int(math.log2(n))

value=minimax(0,0,True,scores,treeDepth)


alpha_beta_pruning(0,0,True,scores,treeDepth,-math.inf,math.inf)



print(f"Total evaluated vertecies in minimax :{minmax_count}")
print(f"The optimal value is: {value}")



print(f"The total evaluated vertecies in alpha_beta :{pruning_count}")



efficiency=((minmax_count-pruning_count)/minmax_count)*100

print(f"\nThe efficiency is: {efficiency}")