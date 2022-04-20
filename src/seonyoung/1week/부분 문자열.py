

# def getPattern(pattern):
#     j=0
#     for i in range(1, len(pattern)):
#         while j>0 and pattern[i]!= pattern[j]:
#             j=pattern[j-1]
#         if pattern[i]==pattern[j]:
#             j+=1
#             pattern[i]=j


# def kmpAlgorithm(tempString, pattern):
#     getPattern(pattern)
#     j=0
#     for i in range(len( tempString)):
#         while (j>0 and tempString[i]!= pattern[j]):
#             i= pattern[j-1] 
#         if tempString[i] ==pattern[j]:
#             if j==len(pattern)-1:
#                 return True
#             else:
#                 return False

inputString=input()
inputPattern = input()
# pattern = [0 for i in range(len(inputPattern))]

if (inputPattern in inputString) == True: 
    print('1')
else :
    print('0')
# if :
#     print('1')
# else:
#     print('0')


