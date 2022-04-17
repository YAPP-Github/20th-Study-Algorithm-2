# 파일정리.py
# Question Link: https://www.acmicpc.net/problem/20291
# Primary idea:     String
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: = ms
# Memory Usage: = MB

dic = dict()

for _ in range(int(input())):
    extension = input().split('.')[1]
    dic[extension] = dic[extension] + 1 if extension in dic else 1
    
for extension, cnt in sorted(dic.items()):
    print(extension, cnt)