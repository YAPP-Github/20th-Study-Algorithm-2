def solution(N, number):
    dp = [[]]
    for i in range(1, 9):
        possible = set()
        strNum = int(str(N)*i)
        possible.add(strNum)
        
        for j in range(1,i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    possible.add(op1+op2)
                    possible.add(op1-op2)
                    possible.add(op1*op2)
                    if op2 != 0:
                        possible.add(op1//op2)
        
        if number in possible:
            return i
        dp.append(possible)
    return -1