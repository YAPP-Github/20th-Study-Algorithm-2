import sys
input = sys.stdin.readline

#어떤 아이스크림의 조합은 맛이 없어짐 -> 모든 경우 피하면서 3가지 선택 -> 3개 다 보기
n, m = map(int, input().split())
icecream = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    icecream[a][b], icecream[b][a] = 1,1

result = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            if not icecream[i][j] and not icecream[j][k] and not icecream[k][i]: #1,2 2,3, 3,1
                result +=1

print(result)