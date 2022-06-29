#https://www.crocus.co.kr/602<-요기를 참조..
from collections import defaultdict

n,k = map(int,input().split())
numList =list(map(int, input().split()))
pfList = defaultdict(int)
count=0

for i in range(1,n):
    numList[i]+=numList[i-1]

for i in range(n):
    if(numList[i]==k):
        count+=1
    count += pfList[numList[i]-k] #(i까지의 부분합-K)이 이전에 있었다면 ++
    pfList[numList[i]] += 1 #i까지 부분합 저장

print(count)