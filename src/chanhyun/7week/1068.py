n = int(input())
tree = map(int, input().split())
erase  = int(input())

def dfs(x, tree):
    tree[x] = -2
    for i in range(n):
        if x == tree[i]:
            dfs(i, tree)

dfs(erase, tree)
count = 0
for i in range(n):
    if tree[i] != -2 and i not in tree:
        count += 1
print(count)