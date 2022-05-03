from collections import deque


n,k =map(int,input().split())
queue = deque()
visited = dict()
samter = list((map(int,input().split())))

for sam in samter:
    queue.append(sam)
    visited[sam]=0

while queue:
    temp = queue.popleft()
    for i in [temp-1,temp+1]:
        if i not in visited and k>0:
            visited[i]=visited[temp]+1
            k-=1
            queue.append(i)


answer=0
for key,value in visited.items():
    answer+=value

print(answer)
