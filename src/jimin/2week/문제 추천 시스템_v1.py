import sys
from heapq import heappush,heappop
input = sys.stdin.readline

problems_min = [] #min heap
problems_max = [] #max heap
delete_problems = []
def recommendation_system(command):
    command_list = command.split(" ")
    while -problems_max[0][1] in delete_problems:
        heappop(problems_max)
    while problems_min[0][1] in delete_problems:
        heappop(problems_min)

    if (command_list[0] == "add"):
        if(int(command_list[1]) in delete_problems):
            delete_problems.remove(int(command_list[1]))
        heappush(problems_min, (int(command_list[2]), int(command_list[1])))
        heappush(problems_max, (-int(command_list[2]), -int(command_list[1])))

    elif(command_list[0] == "recommend"):
        if command_list[1] == "1": #역순 -> max
            print(-problems_max[0][1])
        elif command_list[1] == "-1": #순 -> min
            print(problems_min[0][1])
    elif(command_list[0] == "solved"): #제거
        delete_problems.append(int(command_list[1]))

n = int(input()) #문제 개수
for _ in range(n):
    p,l = map(int, input().split()) #문제 번호, 난이도
    heappush(problems_min, (l, p))
    heappush(problems_max, (-l, -p))

m = int(input()) #명령문 개수
for _ in range(m):
    recommendation_system(input().rstrip())