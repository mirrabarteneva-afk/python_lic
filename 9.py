from random import choice


hirous = input().split()
vs = []
lines = []

for i in hirous:
    for j in hirous[:hirous.index(i)]:
        para = (j, i)
        vs.append(para)

hirous_d = {}
for h in sorted(vs, key=lambda x: hirous.index(x[0])):
    hoic = choice(h)
    lines.append(f'{h[0]} vs {h[1]}: победил {hoic}.\n')
    hirous_d[hoic] = hirous_d.get(hoic, 0) + 1
    
for k, v in hirous_d.items():
    lines.append(f'{k} - {v}\n')
    
with open('tournament.txt', 'w', encoding='utf-8') as tour:
    tour.writelines(lines)