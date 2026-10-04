import csv
from collections import defaultdict
import json

with open('members.csv', encoding='utf-8', newline='') as members, open('council.jsonlines', 'w', encoding='utf-8') as council:
    reader = csv.reader(members)
    header = next(reader)
    name_idx = header.index("name")
    race_idx = header.index("race")

    grouped = defaultdict(list)
    for row in reader:
        race = row[race_idx]
        name = row[name_idx]
        grouped[race].append(name)

    for names in grouped.values():
        names.sort(key=lambda x: (-len(x), x))
    
    result = [{"race": race, "members": members} for race, members in grouped.items()]
    result.sort(key=lambda x: x['race'])
    for i in result:
        json.dump(i, council, ensure_ascii=False)
        council.write('\n')  