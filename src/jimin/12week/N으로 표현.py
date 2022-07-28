# N = 5
# number = 12
N = 2
number = 11
def solution(N, number):
    dp = [set()] #1번째부터 시작하도록 함
    for i in range(1,9): #조합 개수
        numbers = set()
        numbers.add(int(str(N)* i))
        for j in range(1, i):
            for x in dp[j]:
               for y in dp[i-j]:
                   numbers.add(x+y)
                   numbers.add(x-y)
                   numbers.add(x*y)
                   if y != 0:
                       numbers.add(x // y)
        if number in numbers:
            return i
        dp.append(numbers)
    return -1

print(solution(N, number))