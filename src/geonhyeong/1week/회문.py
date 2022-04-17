# 회문.py
# Question Link: https://www.acmicpc.net/problem/17609
# Primary idea:     String, 두 포인터, 
#                   1. 짝수, 홀수 문제인줄 알고 시간을 많이 씀.
#                   2. 풀이
#                       1) 왼쪽 index(left), 오른쪽 index(right)를 각각, -1, 전체길이로 설정
#                       2) flag를 활용하여, 서로 다른점이 없으면 전체 문자열의 '회문'판별
#                       3) left는 + 1, right -1을 하면서 교차할때까지 반복
#                       4) 서로 값이 다를 경우
#                           a) left, right에 위치한 알파벳을 삭제한 문자열 구하기
#                           b) 둘중 하나가 회문이라면, 1
#                           c) 둘중 하나라도 회문이 아니라면, 2
#                       5) 반복문 끝까지 서로 값이 같은 경우
#                           a) 전체 문자열의 '회문'판별
# 
# Time Complexity : O(n^2)
# Space Complexity : O(n)
# Runtime: 500 ms
# Memory Usage: 30840 MB

def isPalindrome(str):
    length = len(str)
    
    for i in range(length//2):
        if str[i] != str[length-i-1]:
            return False
    
    return True

for _ in range(int(input())):
    str = input()
    length = len(str)
    left, right = -1, length
    flag = True

    while left <= right:
        left += 1
        right -= 1

        if str[left] != str[right]:
            newStr1 = str[:left] + str[left+1:]
            newStr2 = str[:right] + str[right+1:]
            print(1 if isPalindrome(newStr1) or isPalindrome(newStr2) else 2)
            flag = False
            break

    if flag:
        print(0 if isPalindrome(str) else 2)