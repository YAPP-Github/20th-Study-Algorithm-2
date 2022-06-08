
n = int(input())
count,max =0,0 
tree =[[] for _ in range(100)]
nodeList = map(int,input().split())
m = int(input())


if m==0:
    print(0)
else :
    for node in nodeList:
        tree[node+1].append(count)
        max=node
        count+=1

    if max ==m:
        max-=1
    for i in range(n):
        if m in tree[i]:
            tree[i].remove(m)
        if n==m:
            tree[n]=[]

    sum=0
    sum+= len(tree[max+1])
    print(sum)