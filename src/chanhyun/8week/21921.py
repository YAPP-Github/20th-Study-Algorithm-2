n, x = map(int, input().split())
visitors = list(map(int, input().split()))

sum = sum(visitors[:x])
max_sum = sum
count = 1
for i in range(1, n-x+1):
    new_sum = sum-visitors[i-1]+visitors[i+x-1]
    if new_sum > max_sum:
        max_sum = new_sum
        count = 1
    elif new_sum == max_sum:
        count += 1
    sum = new_sum

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)