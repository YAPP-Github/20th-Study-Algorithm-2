#16916 부분 문자열, kmp 알고리즘 O(n)
s=input()
p=input()
pi = [0]*len(p)

def getPI(p): #접두사 접미사 일치 정도 확인
    j = 0
    for i in range(1, len(p)):
        while(j>0 and p[i] != p[j]):
            j = pi[j-1]
        if (p[i] == p[j]): #일치하면 j 증가
            j += 1
            pi[i] = j

def kmp(s,p):
    getPI(p)
    j = 0
    for i in range(len(s)):
        while (j>0 and s[i] != p[j]):
            j = pi[j-1]
        if s[i] == p[j]:
            if j == len(p) -1:
                return True
            else:
                j+=1
    return False

if(kmp(s,p)):
    print(1)
else:
    print(0)
