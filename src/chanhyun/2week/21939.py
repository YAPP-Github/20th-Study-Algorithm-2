import heapq

n = int(input())
problems_min = []
problems_max = []
problems_level = dict()
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(problems_min, (l, p))
    heapq.heappush(problems_max, (-l, -p))
    problems_level[p] = l

m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == "recommend":
        if int(command[1]) == 1:
            while -problems_max[0][0] != problems_level[-problems_max[0][1]]: 
                heapq.heappop(problems_max)    
            print(-problems_max[0][1])
        else:
            while problems_min[0][0] != problems_level[problems_min[0][1]]: 
                heapq.heappop(problems_min)   
            print(problems_min[0][1])
    elif command[0] == "solved":
        problems_level[int(command[1])] = 0
    else:
        heapq.heappush(problems_min, (int(command[2]), int(command[1])))
        heapq.heappush(problems_max, (-int(command[2]), -int(command[1])))
        problems_level[int(command[1])] = int(command[2])
