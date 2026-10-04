import json, csv
from collections import defaultdict

rows = []
with open('artifacts.csv', newline='', encoding='utf-8') as artifacts, open('vault.jsonlines', 'w', encoding='utf-8') as vaut:
    artifacts = csv.reader(artifacts)
    header = next(artifacts)
    material_id = header.index('material')
    items_id = header.index('name')
    weight_id = header.index('weight')
    artifacts = sorted(artifacts, key=lambda x: x[weight_id])
    group = defaultdict(list)
    
    for row in artifacts:
        material = row[material_id]
        items = row[items_id]
        group[material].append(items)
        
    result = [{'material': material, 'items': items} for material, items in group.items()]
    result.sort(key=lambda x: x['material'])
    for row in result:
        json.dump(row, vaut, ensure_ascii=False)
        vaut.write('\n')