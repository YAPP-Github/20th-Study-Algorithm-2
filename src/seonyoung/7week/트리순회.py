#전위 순회, 중위순회, 후위순회

def preOrder(tree,root): #전위
    if root!='.':
        print(root, end ='')
        preOrder(tree, tree[root][0])
        preOrder(tree, tree[root][1])

def inOrder(tree,root): #중위
    if root!='.':
        inOrder(tree, tree[root][0])
        print(root, end ='')
        inOrder(tree, tree[root][1])

def postOrder(tree,root): #후위
    if root!='.':
        postOrder(tree, tree[root][0])
        postOrder(tree , tree[root][1])
        print(root, end ='')


n = int(input())
tree = {}

for i in range(n): 
    root, left, right = input().split()
    tree[root] = [left,right]

preOrder(tree, 'A')
print()
inOrder(tree,'A')
print()
postOrder(tree,'A')