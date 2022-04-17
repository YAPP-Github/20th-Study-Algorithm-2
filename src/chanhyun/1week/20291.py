import sys
n = int(sys.stdin.readline())
book = dict()
for _ in range(n):
    file = sys.stdin.readline().strip()
    ext = file.split('.')[1]
    if ext in book:
        book[ext] += 1
    else:
        book[ext] = 1

answer = []
for k, v in book.items():
    answer.append((k,v))
answer.sort()
for a in answer:
    print(a[0], a[1])
