from random import sample


names = ['Питер', 'Сьюзен', 'Эдмунд', 'Люси', 'Юстэс', 'Джил']
result = []
num = int(input())
while len(result) < num:
    rand = sorted(sample(names, 4))
    rand = ', '.join(rand)
    if rand not in result:
        result.append(rand)

print(*result, sep='\n')