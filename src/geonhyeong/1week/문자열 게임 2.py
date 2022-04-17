# 문자열 게임 2.py
# Question Link: https://www.acmicpc.net/problem/20437
# Primary idea:     String, 슬라이딩 윈도우
#                   1. Dictionary(windowList) 이용
#                       1) key : 알파벳
#                       2) value : 알파벳 갯수
#                   2. 풀이
#                       1) K == 1일 경우, "1, 1" 출력
#                       2) cnt >= K : 알파벳의 갯수가 K보다 갯수가 많은 것만 찾기
#                       3) 선택된 알파벳들이 시작하는 index List(startIndex)구하기
#                       4) 범위(0 ~ startIndex)-K+1) : K갯수를 더했을때 out of index가 되는 것까지만
#                       5) i+K-1 : K개를 포함한 index, -1은 마지막 요소의 out of index를 방지하기 위함
#                       6) Dictionary(windowList)에 아무 값이 없을 경우, -1 출력
#                       7) min, max로 최소값 구하기
# 
# Time Complexity : O(n^2)
# Space Complexity : O(n)
# Runtime: 1404 ms
# Memory Usage: 30.84 MB

T = int(input())

for _ in range(T):
    W = input()
    K = int(input())

    dic = dict() # 빈 딕셔너리 선언
    windowList = []

    # 예외처리
    if K == 1:
        print(1, 1)
        continue

    # 알파벳 개수 세기
    for alpha in W:
        dic[alpha] = dic[alpha] + 1 if alpha in dic else 1

    for alpha, cnt in dic.items():
        if cnt >= K:
            startIndex = list(filter(lambda x : W[x] == alpha, range(len(W))))
            
            for i in range(len(startIndex)-K+1): # out of index를 피하기 위함
                windowList.append(startIndex[i+K-1] - startIndex[i])
            
    if not windowList:
        print(-1)
    else:
        print(min(windowList)+1, max(windowList)+1)