# 완전 이진 트리.py
# Question Link: https://www.acmicpc.net/problem/9934
# Primary idea:     String
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 76 ms
# Memory Usage: 30.840 MB

import sys
input = sys.stdin.readline

k = int(input())
numbers = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def binaryTree(arr, depth):
    mid = len(arr) // 2
    tree[depth].append(arr[mid])

    if len(arr) == 1: return

    binaryTree(arr[:mid], depth + 1)
    binaryTree(arr[mid+1:], depth + 1)

binaryTree(numbers, 0)

for i in range(k):
    print(*tree[i])