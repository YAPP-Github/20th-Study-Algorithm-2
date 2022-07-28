citations = [3, 0, 6, 1, 5]
def solution(citations):
    # n편 중에서 h번 이상 인용된 논문이 h편 이상 -> H-index
    citations = sorted(citations)
    left, right = 0, max(citations)
    h_index = 0
    while (left <= right):
        mid = (left + right) // 2
        count = 0
        for citation in citations:
            if citation >= mid:
                count += 1
        if count >= mid:
            left = mid + 1
            h_index = max(h_index, count)
        else:
            right = mid -1
    return h_index

print(solution(citations))