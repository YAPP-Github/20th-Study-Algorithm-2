#21921 블로그
import sys
input = sys.stdin.readline

n, x = map(int, input().split()) #블로그를 시작하고 지난 일수, x일 동안
arr = list(map(int, input().split()))
sub_sum = [0]

#구간 합 구하기
sub_sum_value = 0
for i in arr:
    sub_sum_value = sub_sum_value + i
    sub_sum.append(sub_sum_value)

visitor = []
for i in range(n):
    if(i+x > n):
        break
    visitor.append(sub_sum[x+i] - sub_sum[i])

max_visitor = max(visitor)
if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(visitor.count(max_visitor))


# import sys
# input = sys.stdin.readline
#
# n, x = map(int, input().split()) #블로그를 시작하고 지난 일수, x일 동안
# arr = list(map(int, input().split()))
# arr_visitor = [0] * n
#
# max_visitor = -1
# for i in range(n):
#     visitor = 0
#     if (i+x <= n):
#         for j in range(i, i+x):
#             visitor += arr[j]
#         arr_visitor[i] = visitor
#
# max_visitor = max(arr_visitor)
# if max_visitor == 0:
#     print("SAD")
# else:
#     print(max_visitor)
#     print(arr_visitor.count(max_visitor))




