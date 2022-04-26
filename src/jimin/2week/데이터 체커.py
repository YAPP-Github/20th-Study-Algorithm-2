#22942
#모든 원의 중심 좌표는 x축 위에 존재
#n개의 원 중 임의의 두 원 선택, 교점이 없어야 한다. 즉, 포함하거나 아예 떨어지는게

#1. x 중심으로 정렬
#2. (1)이전 원의 중심 + 반지름 < 다음 원의 중심 - 반지름 (2) 이전 원의 중심 + 반지름 > 다음 원의 중심 + 반지름
# --> X 원 두 개로만 판단하면 안된다..

#0. (()) or ()() 만 가능 -> 스택 이용
#1. 원의 처음, 끝, 원 번호, 처음 끝 저장 (괄호문제와 유사)
#2. 처음 or 끝 지점으로 정렬
#3. 시작이면 스택에 넣고 끝이라면 원의 번호와 비교해서 같으면 pop

n = int(input())
arr=[]
for i in range(n):
    x, r = map(int, input().split())
    arr.append((x-r, i, 0)) #시작 지점, 원 번호
    arr.append((x+r, i, 1)) #끝 지점, 원 번호

arr = sorted(arr)
def data_checker():
    check_stack = []
    for i in arr:
        if i[2] == 0:
            check_stack.append(i)
        else:
            if (check_stack[-1][1] == i[1]):
                check_stack.pop()

    if (len(check_stack) == 0):
        return 'YES'
    else:
        return 'NO'

print(data_checker())