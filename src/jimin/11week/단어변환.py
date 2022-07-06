from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append((begin, 0))

    while queue:
        now_word, count = queue.popleft()
        if now_word == target:
            return count
        for word in words:
            # 한글자만 다른 언어 탐색
            temp = 0
            for i in range(len(word)):
                if word[i] != now_word[i]:
                    temp += 1
            if (temp == 1):  # 한글자만 다른 언어 찾음 그 언어로 변경
                queue.append((word, count + 1))