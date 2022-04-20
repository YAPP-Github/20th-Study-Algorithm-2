#20291

#파일을 확장자 별로 정리해서 몇 개씩 있는지 파악
#포기 편하게 확장자들을 사전 순으로 정렬

n = int(input()) #파일의 개수

result = dict()
for i in range(n):
     file = input().split('.')
     if file[1] not in result.keys(): #확장자가 존재하지 않는다면 새로운 키로 추가 
         result[file[1]] = 1
     else: #확장자가 존재한다면 +1
         result[file[1]] += 1

result = sorted(result.items(), key=lambda x:x[0]) #확장자 순서대로 정렬

#출력
for key, value in result:
    print(key+ ' '+ str(value))
