#1068 트리
#리프 노드의 개수 구하기

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input()) #노드의 개수
arr = list(map(int,input().split())) #각 노드의 부모, 없다면 -1
m = int(input()) #지울 노드의 번호
tree = defaultdict(list)

#딕셔너리로 트리 입력
for i in range(len(arr)):
    if arr[i] == -1: #부모가 없다 -> 루트다
        root = i
        continue
    tree[arr[i]] += [i]

#노드 제거
if m in tree:
    del(tree[m])
for key in tree.keys():
    if (m in tree[key]):
        tree[key].remove(m)

#리프 노드 탐색
leaf_node = set()
def postorder(node):
    global leaf_node
    if len(tree[node]) == 0:
        if node == m:
            return
        leaf_node.add(node)
        return
    for i in range(len(tree[node])):
        postorder(tree[node][i])

postorder(root)
print(len(leaf_node))
