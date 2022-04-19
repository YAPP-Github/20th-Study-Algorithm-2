from re import L


n = int(input())

fileList= {}
for i in range(0,n):
    fileName = input()    
    dotIndex = fileName.find('.') +1
    extension = fileName[dotIndex:]

    if (extension not in fileList): 
        fileList[extension] =1
    else: 
        fileList[extension] +=1
    
    fileList = list(fileList.keys()).sort()
    print(fileList)
    # for temp in fileList:
    #     print(temp, fileList[temp])
