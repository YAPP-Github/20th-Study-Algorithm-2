n = int(input())

answerList  = []
stackList = []
heightList = list(map(int,input().split()))

for i in range(n):

    height = heightList[i]
    while stackList:
        if stackList[-1][1]>height:
            answerList.append(stackList[-1][0]+1)
            break
        else: 
            stackList.pop()
    if not stackList:
        answerList.append(0)
    stackList.append((i,height))


temp=' '.join(map(str,answerList))     
print(temp)