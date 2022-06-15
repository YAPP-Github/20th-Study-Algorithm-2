

def isIncluded(wantedService,serviceList):
    for service in serviceList:
        if service in wantedService:
            wantedService.pop(wantedService.index(service))
    if len(wantedService)==0:
        return True
    else:
        return False

def solution(n, plans, clients):
    answer = [0] * len(clients)

    dataList =[]
    serviceList = []

    for i in range (len(plans)):
        #요금제 표
        tempList = plans[i].split(' ')
        dataList.append(int(tempList[0]))
        newList =list(map(int, tempList[1:]))
        if i>=1:
            serviceList.append(serviceList[i-1]+newList)
        else:
            serviceList.append(newList)

        
    for i in range(len(clients)):
        tempList = clients[i].split(' ')
        wantedData = int(tempList[0])
        watendService = list(map(int,tempList [1:]))
        
        availList = sorted([x for x in dataList if x>=wantedData])

        for j in range (len(availList)):
            index = dataList.index(availList[j]) # 값이 들어있는 인덱스
            isIn = (isIncluded(watendService, serviceList[index]))
            if(isIn):
                answer[i]=index+1
                break                
    return answer



if __name__ == '__main__':
    plans =["100 1 3","500 4","2000 5"]
    clients =["300 3 5","1500 1","100 1 3","50 1 2"]

    answer =solution(5,plans,clients)
