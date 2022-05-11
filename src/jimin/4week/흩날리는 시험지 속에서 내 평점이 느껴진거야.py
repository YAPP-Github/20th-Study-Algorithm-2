#17951
#k 그룹으로 나눈 뒤, 각각의 그룹에서 맞은 개수의 합을 구해서 최소 -> 중의 최대

import sys
input = sys.stdin.readline

def binary_search(start, end):
    result = 0
    while (start <= end):
        mid = (start + end) // 2
        sub_sum = 0
        group_cnt = 0
        for i in range(n):
            sub_sum += solved[i]
            if (sub_sum >= mid):
                sub_sum = 0
                group_cnt += 1
        if sub_sum > mid : # 마지막 그룹에 대해
            group_cnt += 1

        if (group_cnt < k):
            end = mid -1
        else:
            start = mid + 1
            result = mid

    return result


n, k = map(int, input().split()) #시험지 개수, 나눌 그룹 수
solved = list(map(int, input().split()))


print(binary_search(0,20 * n))