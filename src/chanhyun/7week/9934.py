k = int(input())
order = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def make(o, d):
    m = len(o)//2
    tree[d].append(o[m])
    if len(o) == 1:
        return
    make(o[:m], d+1)
    make(o[m+1:], d+1)

make(order, 0)
for i in range(k):
    for x in tree[i]:
        print(x, end=' ')
    print()