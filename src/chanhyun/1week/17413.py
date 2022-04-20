s = input()
answer = ''

i = 0
stack = []
while i < len(s):
    if s[i] == '<':
        while stack:
            answer += stack.pop()
        while s[i] != '>':
            answer += s[i]
            i += 1
        answer += s[i]
        i += 1
        continue
    elif s[i] == ' ':
        while stack:
            answer += stack.pop()
        answer += s[i]
    else:
        stack.append(s[i])
    i += 1

while stack:
    answer += stack.pop()

print(answer)
