#왼쪽에서 출발, 오른쪽에서 출발
#다른 문자가 있다면 둘 중 하나 지우고 비교
import sys
input = sys.stdin.readline

def palindrome(word): #회문 판별
    left = 0
    right = len(word)-1

    while(left < right):
        if(word[left] == word[right] and left < right):
            left += 1; right -= 1
        elif (word[left] != word[right]): #같지 않는 경우
            # 왼쪽 제거
            left_temp = left + 1
            right_temp = right
            left_flag = pop_palindrome(left_temp, right_temp, word)

            # 오른쪽 제거
            left_temp = left
            right_temp = right -1
            right_flag = pop_palindrome(left_temp, right_temp, word)

            if not left_flag or not right_flag:
                return 1
            else:
                return 2
    return 0


def pop_palindrome(left_temp, right_temp, word):
    while (left_temp < right_temp):
        if (word[left_temp] == word[right_temp] and left_temp < right_temp):
            left_temp += 1;
            right_temp -= 1
        else:
            return True
    return False


t = int(input())
for i in range(t):
    print(palindrome(input().rstrip()))
