

from collections import deque


dx , dy = [-1,1,0,0],[0,0,-1,1]

def saveBomb():
    for i in range(r):
        for j in range(c):
            if map[i][j]!='.':
                bombList.append((i,j)) #폭탄 좌표 저장


def insertBomb():
    for i in range(r):
        for j in range(c):
            if map[i][j]!='0':
                map[i][j]='0'


def bomb():
    while bombList:
        x,y =bombList.popleft()
        map[x][y]='.'
        for i in range(4): #앞뒤양옆 폭탄 터짐
            nx, ny= x+dx[i], y+dy[i]
            if 0<=nx< r and 0 <= ny<c:
                if map[nx][ny] =='0':
                    map[nx][ny]='.'


def printMap():
    for i in range(r):
        for j in range(c):
            print(map[i][j],end=' ')
        print()


if __name__ == '__main__':
    r,c,time = map(int,input().split())
    map = [list(input()) for _ in range(r)]
    bombList =deque()
    time-=1 #1초 동안 아무것도 안함

    while time>0 : 
        saveBomb()
        insertBomb()
        time-=1 #1초동안 폭탄 설치
        if time==0:
            break
        bomb()
        time-=1 #3초전 설치된 폭탄이 모두 폭발

    printMap()