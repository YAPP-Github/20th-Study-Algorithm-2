#tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
tickets = [["ICN","A"], ["ICN", "B"], ["B", "ICN"]]
#tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
from collections import defaultdict
import heapq

def dfs(ticket_dict, v, answer):
    while ticket_dict[v]:
        to_c = heapq.heappop(ticket_dict[v])
        dfs(ticket_dict, to_c, answer)
    if(len(ticket_dict[v]) == 0): #모두 방문 가능, 방문할 수 없다면 경로에 넣기
        answer.append(v)
        return

def solution(tickets):
    answer = []
    ticket_dict = defaultdict(list)
    for ticket in tickets:
        from_c, to_c = ticket
        ticket_dict[from_c].append(to_c)

    for key, value in ticket_dict.items():
        ticket_dict[key] = sorted(value)
    dfs(ticket_dict, "ICN", answer)

    return answer[::-1]

print(solution(tickets))