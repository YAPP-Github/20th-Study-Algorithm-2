

n,m = map(int, input().split())
count=0

if(n==3):
    print(count)
else:
    nopeList = [[False] * (n+1) for _ in range(n+1)]

    for i in range(m):
        i,j = map(int,input().split())
        nopeList[i][j]=True
        nopeList[j][i]=True

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1,n):
                if nopeList[i][j]==False and nopeList[j][k]==False and nopeList[i][k]==False: #안되는 조합에 해당하지 않는 경우
                    count+=1
    print(count)

    
