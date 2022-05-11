#19637
import sys
input = sys.stdin.readline

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (powers[mid] == target):
            return names[mid]
        elif (powers[mid] > target):
            end = mid - 1
        elif (powers[mid] < target):
            start = mid + 1
    return names[start]


n, m = map(int, input().split()) #칭호 개수, 칭호를 출력해야 하는 캐릭터 개수
powers = []
names = []
for i in range(n):
    name = input().split(" ")
    if (len(powers)> 0 and powers[-1] == int(name[1])):
        continue
    names.append(name[0])
    powers.append(int(name[1]))

for i in range(m):
    print(binary_search(int(input()), 0, len(powers)-1))
