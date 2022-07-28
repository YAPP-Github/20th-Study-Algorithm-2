def NtoK(n, k):
    result = ""
    while n > 0:
        result = str(n % k) + result
        n //= k
    return result

def isPrime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    result = NtoK(n,k)
    nums = result.split('0')
    for num in nums:
        if num != "" and isPrime(int(num)):
            answer += 1
    return answer