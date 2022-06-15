#22862
#짝수로 이루어진 연속한 부분 수열 중 가장 긴 길이
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) #수열 s 길이, 삭제할 수 있는 최대 횟수
s = list(map(int, input().split()))

answer_length = 0 #전체 길이
temp_length = 0 #부분적으로 구하는 길이
delete_cnt = 0 #삭제 수

left, right = 0, 0 #시작점, 끝 점
while(right < n and left <= right):
    if (delete_cnt <= k):
        if (s[right] %2 == 0):
            temp_length += 1
        else:
            delete_cnt += 1
        right += 1

    else:
        if(s[left] %2 == 1):
            delete_cnt -= 1
        else:
            temp_length -= 1
        left += 1
    answer_length = max(answer_length, temp_length)

print(answer_length)
