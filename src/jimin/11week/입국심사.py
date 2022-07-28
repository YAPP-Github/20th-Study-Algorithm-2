def solution(n, times):
    left = 1
    right = max(times) * n
    while (left <= right):
        mid = (left + right) // 2
        people_cnt = 0
        for time in times:
            people_cnt += mid // time
            if (people_cnt >= n):
                break
        if people_cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer