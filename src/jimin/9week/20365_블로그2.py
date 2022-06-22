#20365
import sys
input = sys.stdin.readline

n = input()
colors = list(input().strip())
answer = {'R':1, 'B':1}

pre_color = ''
for color in colors:
    if color != pre_color:
        answer[color] += 1
    pre_color = color

if(answer['R']> answer['B']):
    print(answer['B'])
else:
    print(answer['R'])
