#괄호가 들어간 모든 조합을 구하기 위해서 python combination 라이브러리 사용
# ** 사용하는 케이스 ** 
# 하나의 리스트에서 모든 조합을 계산을 할 때 ->  permutations, combinations을 사용
# 두개 이상의 리스트에서 모든 조합을 계산해야 할 때 -> product를 사용
# lsit to string : ''.join(list)

from itertools import combinations


bracketString = input()
stack= []
indexList=[]

answerList= set()

for i in range(len(bracketString)):    
    if(bracketString[i]=='('):
        stack.append(i)
    elif(bracketString[i]==')'):
        start = stack.pop()
        end = i
        indexList.append([start,end])


for i in range(1,len(indexList)+1):
    combList = list(combinations(indexList,i))
    
    for combination in combList:
        temp = list(bracketString)
        
        for bracketIndex in combination:
            start, end = bracketIndex            
            temp[start] = ''
            temp[end]=''
            
        temp = ''.join(temp)
        answerList.add(temp)

answerList = sorted(list(answerList))
for answer in answerList:
    print(answer)