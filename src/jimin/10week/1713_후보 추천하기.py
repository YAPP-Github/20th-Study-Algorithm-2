#1713 후보 추천하기
import sys
import math
from collections import defaultdict
input = sys.stdin.readline

n = int(input()) #사진 틀
total = int(input()) #전체 학생 수
students = list(map(int,input().split())) #추천 받은 학생 목록

count = defaultdict(int)
album = []
for student in students:
    count[student] += 1

    if (student in album):
        continue

    if len(album) < n:
        album.append(student)

    else:
        min_student_count = math.inf
        min_student = -1
        for album_student in album:
            if (count[album_student] < min_student_count):
                min_student_count = count[album_student]
                min_student = album_student
        album.remove(min_student)
        count[min_student] = 0
        album.append(student)


print(*sorted(album))