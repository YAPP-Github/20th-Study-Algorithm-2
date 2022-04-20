
import sys 
input = sys.stdin.readline 

n=int(input())
file={}

for i in range(n): 
    fileName = input()    
    dotIndex = fileName.find('.') +1
    extension = fileName[dotIndex:-1]
    file[extension] = file.get(extension, 0) + 1 
for value in sorted(file.items()): 
    print(value[0], value[1])
