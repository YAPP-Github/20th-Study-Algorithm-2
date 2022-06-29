#20922 겹치는 건 싫어
import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split()) #길이가 n인 수열, 같은 원소 k개 이하
arr = list(map(int, input().split()))

num_count = defaultdict(int)
left, right = 0, 0
answer = 0

while (right < n):
    r_count = num_count.get(arr[right], 0)
    if (r_count < k): #오른쪽 확장 가능
        num_count[arr[right]] += 1
        right += 1

    else: #크면 안되니까 ... left 일단 땡겨
        num_count[arr[left]] -= 1
        left += 1
    answer = max(answer, right-left)

print(answer)