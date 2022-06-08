import sys
from collections import defaultdict
input = sys.stdin.readline

#완전 이진 트리
#마지막 레벨 제외, 모든 레벨이 완전히 채워져 있음
#왼쪽에서 오른쪽으로 채워져야 함

#조건 읽어보니까 중위 탐색
k = int(input()) #깊이
path = list(map(int,input().split()))

tree = defaultdict(list)
def tree_solution(start, end, depth):
    if start == end:
        tree[depth] += [path[start]]
        return
    mid = (start + end) // 2
    tree[depth] += [path[mid]]
    tree_solution(start, mid-1, depth+1) #왼쪽
    tree_solution(mid+1, end, depth+1) #오른쪽

tree_solution(0, len(path)-1, 1)
for item in tree.items():
    print(*item[1])