#orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
#course = [2,3,4]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    for c in course:
        order_list = []
        for order in orders:
            combi = combinations(sorted(order), c)
            order_list += combi

        counter = Counter(order_list)

        for key, value in counter.items():
            if (value >= 2):
                if value == max(counter.values()):
                    result.append("".join(key))
    return sorted(result)

print(solution(orders, course))