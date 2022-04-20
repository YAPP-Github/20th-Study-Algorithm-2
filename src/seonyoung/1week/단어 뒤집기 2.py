#isalnum 알파벳 또는 숫자인지 확인하는 함수
from audioop import reverse
from curses.ascii import isalnum
from tempfile import tempdir


tempString = str(input())
max =len(tempString)

i=0

while i<max:
    if(tempString[i]=='<'):
        i+=1
        while(tempString[i]!='>'):
            i+=1
        i+=1

    elif( tempString[i].isalnum()==True):
        start= i
        while( (tempString[i].isalnum()==True) and i<max ):
            #문자열의 끝이거나 숫자나 알파벳이 아닐 경우에
            i+=1
        temp= tempString[start:i]
        reverse=temp[::-1]

        ####여기서 왜 적용안되는지 몰겠삼
        # tempString[start:i]=temp[0:len(temp)]
        tempString=tempString.replace(temp,reverse)

    else:
        i+=1

print(tempString)
