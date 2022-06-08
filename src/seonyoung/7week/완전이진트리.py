def findRoot(treeString,count):
    if len(treeString)==1:
        tree[count].append(treeString[0])        
        return
    mid = len(treeString)//2
    tree[count].append(treeString[mid])
    # del treeString[mid] #중간값 지우기
    count+=1
    findRoot(treeString[:mid],count)
    findRoot(treeString[mid+1:],count)
    


n = int(input())
tree = [[] for _ in range(n)]
treeString = list(input().split())
findRoot(treeString,0)

for node in tree:
    print(*node)