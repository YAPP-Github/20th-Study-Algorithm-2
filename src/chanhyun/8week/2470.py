n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

l = 0
r = n-1
min_value = 1e9*2
answer = []
while l<r:
    value = liquid[l]+liquid[r]
    if abs(value) < min_value:
        min_value = abs(value)
        answer = [l,r]
    
    if value < 0:
        l += 1
    else:
        r -= 1

print(liquid[answer[0]], liquid[answer[1]])
