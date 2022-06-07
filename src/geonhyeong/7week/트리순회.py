# 트리순회.py
# Question Link: https://www.acmicpc.net/problem/1991
# Primary idea:     트리
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 76 ms
# Memory Usage: 30.840 MB

import sys
input = sys.stdin.readline

n = int(input())
tree = {}

# 입력
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위
def preorder(root):
    if root != '.':
        print(root, end='')         # root
        preorder(tree[root][0])     # left
        preorder(tree[root][1])     # right

# 중위
def inorder(root):
    if root != '.':
        inorder(tree[root][0])      # left
        print(root, end='')         # root
        inorder(tree[root][1])      # right
 
 # 후위
def postorder(root):
    if root != '.':
        postorder(tree[root][0])    # left
        postorder(tree[root][1])    # right
        print(root, end='')         # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')