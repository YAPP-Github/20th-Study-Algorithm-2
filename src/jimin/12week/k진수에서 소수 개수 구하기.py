#n, k = 437674, 3
n, k = 110011, 10

def isPrime(n):
    if(n == 1):
        return False
    for i in range(2,  int(n**(1/2)+1)):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    temp_answer = ""
    while(n > k):
        temp_answer = str(n % k) + temp_answer
        n //= k
    temp_answer = str(n) + temp_answer
    answer = 0
    for temp in temp_answer.split('0'):
        if temp == '':
            continue
        if isPrime(int(temp)):
            answer += 1

    return answer

print(solution(n,k))
