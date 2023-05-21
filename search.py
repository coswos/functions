# линейный поиск
exm = 'hello my brooo'
compare = 'o'
for i in range(1, len(exm)):
    if exm[i] == compare:
        print('index:', i, exm[i])

# чем больше строка, тем быстрее будет поиск (непонятный пока)
exm = 'hello my brooo'
compare = 'o'
start_index = 0
while (find_index := exm.find(compare, start_index)) != -1:
    print(find_index)
    start_index = find_index + 1