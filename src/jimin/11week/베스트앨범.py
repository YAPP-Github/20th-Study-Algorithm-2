def solution(genres, plays):
    genres_dict = dict()
    sum_dict = dict()
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if (genre in genres_dict.keys()):
            genres_dict[genre].append((play, i))
            sum_dict[genre] += play
        else:
            genres_dict[genre] = [(play, i)]
            sum_dict[genre] = play

    sum_dict = sorted(sum_dict.items(), key=lambda x: -x[1])

    answer = []
    for key, value in sum_dict:
        result = sorted(genres_dict[key], key=lambda x: -x[0])
        answer.append(result[0][1])
        if len(result) >= 2:
            answer.append(result[1][1])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))