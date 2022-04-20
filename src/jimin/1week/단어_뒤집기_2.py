#단어뒤집기 17413
word = input()

answer_word = "" #전체 answer
part_word = "" #부분 answer

tag_flag = False #태그 판별 필요, tag 시작(<)일 때 표시
for i in word:
    if not tag_flag:
        if i == "<":
            tag_flag = True
            part_word += i
        elif i == " ":
            part_word += i
            answer_word += part_word
            part_word = ""
        else:
            part_word = i + part_word
    elif tag_flag:
        if i == ">":
            tag_flag = False
            part_word += i
            answer_word += part_word
            part_word = ""
        else:
            part_word += i

print(answer_word + part_word)
