from collections import deque

n,m,k = map(int, input().split())

A= [list(map(int, input().split())) for _ in range(n)]
board = [[5]*n for _ in range(n)]
treeDict = {(i,j): deque() for i in range(n) for j in range(n)}

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for i in range(m):
    x,y,age = list(map(int,input().split()))
    treeDict[(x-1,y-1)].append(age)

for year in range(k):
    #봄
    for (x,y), trees in treeDict.items():
        survive = deque()
        sumv =0
        for tree in trees :
            if tree <= board[x][y]:
                board[x][y] -=tree
                survive.append(tree+1)
            else:
                sumv+=tree//2
        treeDict[(x,y)] = survive
        board[x][y] +=sumv
    #가을
    newTree=[]
    for (x,y) ,trees in treeDict.items():
        for tree in trees:
            if tree%5==0:
                for i in range(8):
                    nx,ny= x+dx[i],y+dy[i]
                    if not (0<=nx<n and 0<=ny<n):
                        continue
                    newTree.append((nx,ny))
    for x,y in newTree:
        treeDict[(x,y)].appendleft(1)
    #겨울
    for i in range(n):
        for j in range(n):
            board[i][j] +=A[i][j]

count=0
for trees in treeDict.values():
    count+= len( trees)
print(count)
