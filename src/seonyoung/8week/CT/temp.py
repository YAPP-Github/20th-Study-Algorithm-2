#1

def solution(p):
    answer = [0]*len(p)
    
    print(answer)

    print (p)
    print(p[1:])
    for i in range (len(p)):
        for j in range(i+1,len(p)):
            if(p[i]>p[j]):
               index = p.index(min(p[j:]))
               temp = p[i]
               p[i]=p[index]
               p[index]=temp
               answer[i]+=1
               answer[index]+=1
    return answer

if __name__ == '__main__':
    p =[2, 5, 3, 1, 4]
    answer =solution(p)
    print(answer)