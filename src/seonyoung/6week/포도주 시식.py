
n = int(input())
wineList = [0] 
for i in range(n):
    wineList.append(int(input()))

maxList=[0]
maxList.append(wineList[1])
maxList.append( wineList[1]+wineList[2])

#i-1: i번째 와인잔을 택하지 않았을 경우
#i-2, wine[i] : 이전와인잔 포기 + 현재 와인잔 선택
#i-3, wine[i-1], wine[i] : 현재와 이전 와인잔 선택 + 전전 값
for i in range(3,n+1):
    maxList.append(max(maxList[i - 1], maxList[i - 2] + wineList[i], maxList[i - 3] + wineList[i - 1] + wineList[i]))


print(maxList[n])
