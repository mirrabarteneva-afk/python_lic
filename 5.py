def travel(file_name, key=max):
    with open(file_name, 'r', encoding='utf-8') as file_name:
        data = [list(map(lambda x: int(x), x.rstrip().split())) for x in file_name]
    
    start_end = data[0][0] + data[-1][-1]
    if key == max:
        for ind, line in zip(range(len(data) - 1), data):
            for i in range(len(line) - 1):
                if line[i + 1] < data[ind + 1][i]:
                    print(data[ind + 1][i])
                    i = i + 1
                else:
                    print(line[i + 1])
                    i = i + 1
print(travel('map.txt', key=max))
