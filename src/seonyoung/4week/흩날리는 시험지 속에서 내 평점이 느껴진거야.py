# https://www.acmicpc.net/problem/17951
#각 그룹의 합이 mid 이상이 되도록 전체 시험지를 k개 그룹으로 나누는 문제
#결정문제 => 파라메트릭 서치 


n,k = map(int, input().split())
scoreList = list(map(int, input().split()))

left,right=0,20*n
while left<=right:
    mid= (left+right)//2
    group,score =0,0
    for tempScore in scoreList:
        score +=tempScore
        if score>=mid:
            group+=1
            score=0
    
    if group>=k:
        answer = mid
        left =mid+1
    else:
        right=mid-1

print(answer)