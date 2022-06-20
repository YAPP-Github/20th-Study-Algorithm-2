h,w = map(int, input().split())
waterList = list(map(int, input().split()))

left, right = 0, w - 1
max_left = waterList[left]
max_right = waterList[right]

result = 0

while left < right:
    max_left = max(max_left, waterList[left])
    max_right = max(max_right, waterList[right])
    
    if max_left >= max_right:
        result += max_right - waterList[right]
        right -= 1
    elif max_left < max_right:
        result += max_left - waterList[left]
        left += 1

print(result)