#2
def isVip(period, paySum):
    #vip인지 판별
    if(period>=24 and paySum>=900000):
        return True
    elif(period>=60 and 600000<=paySum<900000):
        return True
    else: 
        return False

def solution(periods, payments, estimates):
    answer =[0,0]
    for i in range (len(periods)):
        paySum = sum(payments[i])
        nextPaySum = sum(payments[i][1:])+estimates[i]

        isNowVip= isVip(periods[i],paySum)
        isNextVip = isVip(periods[i]+1,nextPaySum) 

        if isNowVip != isNextVip:
            if isNextVip == True :
                answer[0]+=1
            else :
                answer[1]+=1
    return answer


if __name__ == '__main__':
    answer =solution(p)
    print(answer)