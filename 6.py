import csv


def load_kings(file_name):
    with open(file_name, newline='', encoding='utf-8') as cronicle:
        reader = csv.reader(cronicle)
        next(reader)
        cronicle = [
            (x[0], int(x[1]), int(x[2]))
            for x in [
                x.split(';')
                for y in reader
                for x in y
            ]
        ]
        return cronicle


def filter_by_century(kings: list, century: int):
    kings_cent = []
    for t in kings:
        if (
            (t[1] <= century * 100 <= t[2])
            or (t[1] in range(century * 100 - 99, century * 100))
            or (t[2] in range(century * 100 - 99, century * 100))
        ):
            kings_cent.append(t)
    return [x[0] for x in sorted(kings_cent, key=lambda x: x[0])]


def longest_ruling(kings, n):
    kings = sorted(
        kings,
        key=lambda x: (-(x[2] - x[1]), x[0])
    )[:n]
    return [x[0] for x in kings]


def report(kings):
    durations = [x[2] - x[1] for x in kings]
    sr = sum(durations) // len(durations)
    longest = sorted(
        kings,
        key=lambda x: (-(x[2] - x[1]), x[0])
    )[0][0]
    return (
        f'Всего правителей: {len(kings)}\n'
        f'Средняя длина правления: {sr + 1} лет\n'
        f'Самый долгий правитель: {longest}'
    )

kings = load_kings('cronicle.csv')
print(report(kings))
print('-' * 20)
print('10 longest ruling kings:')
print(*longest_ruling(kings, 10), sep=', ')