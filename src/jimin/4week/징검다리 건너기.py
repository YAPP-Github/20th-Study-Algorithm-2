#22871, 징검다리 건너기
import sys
input = sys.stdin.readline

def binary_search(start, end):
    while (start <= end):
        mid = (start + end) // 2
        visited = [False] * (n + 1) #징검다리 표시
        visited[1] = True
        for i in range(1, n+1):
            if(visited[-1]): #마지막 도달
                break
            if (visited[i]):
                for j in range(i+1, n+1):
                    power = (j-i) * (1 + abs(arr[j] - arr[i]))
                    if ( power < mid):
                        visited[j] = True
        if (visited[-1]): #징검다리 도착 -> mid 값 작아지도록
            end = mid -1
        else:
            start = mid +1
    return end

n = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr

print(binary_search(0, 1000000))