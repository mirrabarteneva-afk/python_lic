def arsenal(*weapon):
    sr = sum(tuple(map(lambda x: len(x), weapon))) // len(tuple(map(lambda x: len(x), weapon)))
    result = [x[0].upper() + x[1:] for x in weapon]
    return sorted(set(filter(lambda x: len(x) <= sr, result)))

weapon = ['javelin', 'andurilflameofthewest', 'javelin', 'glamdring', 'breastplate', 'narsil', 'helmet', 'sting', 'pauldrons', 'dunedainsword', 'scabbard', 'wingedcrown', 'warhammer']
print(*arsenal(*weapon), sep='\n')