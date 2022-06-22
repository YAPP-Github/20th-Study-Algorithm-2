h, w = map(int, input().split())
heights = list(map(int, input().split()))

left = [0 for _ in range(w)]
right = [0 for _ in range(w)]

max_left = heights[0]
for i in range(w):
    if heights[i] > max_left:
        max_left = heights[i]
    left[i] = max_left

max_right = heights[w-1]
for i in range(w-1, -1, -1):
    if heights[i] > max_right:
        max_right = heights[i]
    right[i] = max_right

answer = 0
for i in range(w):
    answer += min(left[i], right[i]) - heights[i]

print(answer)