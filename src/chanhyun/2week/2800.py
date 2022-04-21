def makeExp(contain):
    str = ''
    for i in range(len(exp)):
        if i not in contain:
            str += exp[i]
    if str not in answer:
        answer.append(str)

def makeCases(contain, i):
    if i == len(indexes):
        if contain != []:
            makeExp(contain)
        return
    contain.append(indexes[i][0])
    contain.append(indexes[i][1])
    makeCases(contain, i+1)
    contain.remove(indexes[i][0])
    contain.remove(indexes[i][1])
    makeCases(contain, i+1)
    return contain

exp = input()
answer = []

stack = []
indexes = []
for i in range(len(exp)):
    if exp[i] == '(':
        stack.append(i)
    elif exp[i] == ')':
        j = stack.pop()
        indexes.append([j,i])

makeCases([], 0)

answer.sort()
for a in answer:
    print(a)