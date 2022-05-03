
#인접한 노드를 구해주는 문제인 것 같아서 너비우선탐색인 BFS를 사용해서 푸었습니다!
#거리가 2이상 3이하인 노드의 갯수를 출력해줍니다. 

from collections import deque


def bfs(startNode):
    answer=0
    queue=deque([[startNode,0]])

    while queue : 
        nowNode,dist = queue.popleft()
        if dist<=2:
            answer+=1
        for nextNode in graph[nowNode]:
            if not visited[nextNode]:
                visited[nextNode] =1
                queue.append([nextNode,dist+1])
    return answer-1



friendsNum = int(input())
listNumber = int(input())
graph =[[] for _ in range(friendsNum+1)] 

for i in range (listNumber):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(listNumber+1)]
visited[1]=1 #방문한 노드 1 체크

answer = bfs(1)
print(answer)

