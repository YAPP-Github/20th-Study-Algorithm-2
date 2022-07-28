# .py
# Question Link: 
# Primary idea:     String
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

from itertools import combinations

def solution(orders, course):
    answer = []

    for size in course:
        course_dict = dict()

        for order in orders:
            order_arr = combinations(sorted(list(order)), size)

            for item in order_arr:
                course_dict[item] = course_dict[item] + 1 if item in course_dict else 1

        course_dict = sorted(course_dict.items(), reverse=True, key=lambda x:x[1])

        maxSize = 2
        for key, value in course_dict:
            if (value >= maxSize):
                maxSize = value
                answer.append(''.join(list(key)))

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])) # ["AC", "ACDE", "BCFG", "CDE"]
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])) # ["ACD", "AD", "ADE", "CD", "XYZ"]