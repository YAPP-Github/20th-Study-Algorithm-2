import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for i in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)

#전위 순회, root -> left -> right
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

#중위 순회, left -> root -> right
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

#후위 순회, left -> right -> root
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
