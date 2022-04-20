import sys
input = sys.stdin.readline
from collections import defaultdict


n = int(input())
for i in range(n):
    w = input()
    k = int(input())
    
    if k==1:
        print(1,1)
    charList = defaultdict(int) #각각 알파벳 나온 숫자 카운트
    interval= []

    for i in w:
        charList[i] +=1
    for key, value in charList.items():
        if (value>=k):
            tempList = list(filter(lambda x:w[x]==key,range(len(w))))
            for j in range(len(tempList)-k+1):
                interval.append(tempList[j+k-1]-tempList[j])
        
    if not interval:
        print(-1)
    print (min(interval)+1, max(interval)+1)

    