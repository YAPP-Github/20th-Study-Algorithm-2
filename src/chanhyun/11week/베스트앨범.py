def solution(genres, plays):
    answer = []
    genre_count = dict()
    genre_list = dict()
    for i in range(len(genres)):
        if genres[i] in genre_count:
            genre_count[genres[i]] += plays[i]
            genre_list[genres[i]].append((plays[i],i))
        else:
            genre_count[genres[i]] = plays[i]
            genre_list[genres[i]] = [(plays[i],i)]
    for g in genre_list:
        genre_list[g].sort(key=lambda x: (-x[0],x[1]))
    gc = []
    for k,v in genre_count.items():
        gc.append((v,k))
    gc.sort(reverse=True)
    for g in gc:
        answer.append(genre_list[g[1]][0][1])
        if len(genre_list[g[1]]) > 1:
            answer.append(genre_list[g[1]][1][1])
    return answer