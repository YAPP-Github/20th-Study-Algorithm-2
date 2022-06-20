#6416 트리인가?
#u: 나가는 간선, v: 들어오는 간선
#들어오는 간선이 없다면 루트 노드, 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선 존재
import sys
from collections import defaultdict
input = sys.stdin.readline

def condition_1(u_list):
    #들어오는 간선이 하나도 없는 단 하나의 노드 존재
    key_count = 0
    for k in tree.keys():
        for v in tree.values():
            if k in v:
                key_count += 1
                if k in u_list:
                    u_list.remove(k)

    if len(u_list) == 0:
        return False
    else:
        return u_list.pop()

def condition_2():
    #루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재
    for v_list in tree.values():
        for v in v_list:
            if v_count[v] > 1:
                return False
    return True

def condition_3(node):
    tree_check(node)
    for v in visited.keys():
        if visited[v] == 0: #방문하지 않은게 있다면
            return False
    return True

def tree_check(node):
    if node in visited.keys():
        visited[node] += 1
    for i in range(len(tree[node])):
        tree_check(tree[node][i])


def print_result(count, isTree):
    if isTree:
        print(f"Case {count} is a tree.")
    else:
        print(f"Case {count} is not a tree.")

tree = defaultdict(list) #트리 딕셔너리
v_count = defaultdict(int) #들어오는 간선 카운트
u_list = set() #나가는 간선
visited = dict() #방문 여부
count = 1
while(1):
    isTree = True
    input_case = input().rstrip()
    if(input_case == "-1 -1"):
        break

    case = list(map(int, input_case.split()))

    case_flag = False
    for i in range(0, len(case), 2):
        if case[i] == 0 and case[i+1] == 0 and len(tree) > 0:
            case_flag = True
            break
        elif case[i] == 0 and case[i+1] == 0 and len(tree) == 0:
            print_result(count, True)
            count += 1
        else:
            v_count[case[i + 1]] += 1
            tree[case[i]] += [case[i+1]]
            u_list.add(case[i])
            visited[case[i]] = 0
            visited[case[i+1]] = 0

    if case_flag:
        root = condition_1(u_list)
        if root == False:
            isTree = False
        if not condition_2():
            isTree = False
        if not condition_3(root):
            isTree = False

        #출력 후 리셋
        print_result(count, isTree)
        tree = defaultdict(list)
        v_count = defaultdict(int)
        u_list = set()
        visited = dict()
        count += 1
