from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i,j))
        elif city[i][j] == 2:
            chickens.append((i,j))

cases = list(combinations(chickens, m))
answer = 2*n*2*n
for case in cases:
    city_chicken_distance = 0
    for h in houses:
        chicken_distance = 2*n
        for c in case:
            distance = abs(h[0]-c[0])+abs(h[1]-c[1])
            chicken_distance = min(chicken_distance, distance)
        city_chicken_distance += chicken_distance
    answer = min(answer, city_chicken_distance)

print(answer)