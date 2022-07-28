from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    for c in course:
        customers = []
        for i in range(len(orders)):
            cases = list(combinations(orders[i], c))
            for case in cases:
                case = list(case)
                case.sort()
                customers.append("".join(case))
        menus = set(customers)
        count = defaultdict(list)
        for menu in menus:
            c = customers.count(menu)
            count[c].append(menu)
        maxCount = 0
        for k,v in count.items():
            maxCount = max(maxCount, k)
        maxCountMenus = count[maxCount]
        if maxCount > 1:
            answer += maxCountMenus
    answer.sort()
    return answer