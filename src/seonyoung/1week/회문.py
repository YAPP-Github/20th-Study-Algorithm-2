input = sys.stdin.readline

def isLeftHalf(tempString):
    tempString=tempString[1:]
    if((tempString==tempString[::-1])==True):
        return True
    else: 
        return False

def isRightHalf(tempString):
    tempString=tempString[:-1]
    if((tempString==tempString[::-1])==True):
        return True
    else: 
        return False



if __name__ == "__main__" :
    n = int(input())
    
    for i in range(0,n):
        tempString =input()
        while(len(tempString)>0):
            if(tempString[0]==tempString[-1]):
                if(len(tempString)==2):
                    print('0')
                    break
                tempString=tempString[1:-1]
            else:
                #같지 않은 겨웅
                left =isLeftHalf(tempString) 
                right =isRightHalf(tempString)
                if left==True or right==True:
                    print('1')
                    break
                else:
                    print('2')
                    break
        