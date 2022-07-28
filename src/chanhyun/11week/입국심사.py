def solution(n, times):
    answer = n*times[-1]+1
    times.sort()
    start = 1
    end = n*times[-1]
    while start <= end:
        mid = (start+end) // 2
        count = 0
        for t in times:
            count += mid // t
            if count >= n:
                break
        if count >= n:
            answer = min(answer, mid)
            end = mid-1
        else:
            start = mid+1
    return answer