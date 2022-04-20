# 파일정리.py
# Question Link: https://www.acmicpc.net/problem/20291
# Primary idea:     String
#                   1. split으로 '.'을 기준으로 나눈 뒤, 2번째 요소(확장자)를 추출
#                   2. dictionary에 값을 누적
#                   3. dictionary key값을 기준으로 오름차순
# 
# Time Complexity : O(n)
# Space Complexity : O(n)
# Runtime: 2152 ms
# Memory Usage: 43.64 MB

dic = dict()

for _ in range(int(input())):
    extension = input().split('.')[1]
    dic[extension] = dic[extension] + 1 if extension in dic else 1
    
for extension, cnt in sorted(dic.items()):
    print(extension, cnt)