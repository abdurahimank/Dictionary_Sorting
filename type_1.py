snake = [[4, 4], [4, 2], [2, 1], [1, 0], [0, 0], [0, 2]]
computer = [[2, 5], [3, 5], [0, 5]]
dominoes = [j for i in snake + computer for j in i]
score_dict = {}
for i in computer:
    score_dict[tuple(i)] = dominoes.count(i[0]) + dominoes.count(i[1]) if i[0] != i[1] else dominoes.count(i[0])
print(score_dict)
dict_sorted = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
print(dict_sorted)
