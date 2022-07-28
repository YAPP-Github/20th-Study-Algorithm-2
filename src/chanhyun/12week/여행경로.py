from collections import defaultdict

def solution(tickets):
    answer = []
    trips = defaultdict(list)
    for t in tickets:
        trips[t[0]].append([t[1],False])
    for k,v in trips.items():
        v.sort()
    def dfs(route, trips, count):
        if count == 0:
            answer.append(" ".join(route))
            return
        if route[-1] not in trips:
            return
        for dst in trips[route[-1]]:
            if not dst[1]:
                dst[1] = True
                route.append(dst[0])
                dfs(route, trips, count-1)
                route.pop()
                dst[1] = False
    dfs(["ICN"],trips,len(tickets))
    answer.sort()
    return answer[0].split()