import csv
import json
from collections import defaultdict


def process_treasures(csv_filename, json_filename, secret_key, grouping):
    with open(csv_filename, newline='', encoding='utf-8') as file, \
         open(json_filename, 'w', encoding='utf-8') as j_f:

        reader = csv.reader(file, delimiter='.')
        header = next(reader)
        group = defaultdict(list)
        
        if grouping == 'Quantity':
            for row in sorted(reader):
                total_items = row[header.index(grouping)]
                total_value = row[header.index('Price_in_gold')]
                items = row[header.index('Item')]
                group[total_items].append((total_value, items))
                
            group = {
                'group' + k: {
                    'total_items': int(k) * len(v),
                    'total_value': sum([int(x[0]) for x in v]) * int(k),
                    'items': sorted([x[1] for x in v], reverse=True),
                }
                for k, v in group.items()
            }
            
        elif grouping == 'Price_in_gold':
            for row in sorted(reader):
                total_items = row[header.index(grouping)]
                total_value = row[header.index('Quantity')]
                items = row[header.index('Item')]
                group[total_items].append((total_value, items))
                
            group = {
                'group' + k: {
                    'total_items': sum([int(x[0]) for x in v]),
                    'total_value': int(k) * sum([int(x[0]) for x in v]),
                    'items': sorted([x[1] for x in v], reverse=True),
                }
                for k, v in group.items()
            }
        
        elif grouping == 'Found_in':
            for row in sorted(reader):
                total_items = row[header.index(grouping)]
                total_value = row[header.index('Quantity')]
                items = row[header.index('Item')]
                price = row[header.index('Price_in_gold')]
                group[total_items].append((total_value, items, price))
                
            group = {
                'group' + k: {
                    'total_items': sum([int(x[0]) for x in v]),
                    'total_value': sum([int(x[2]) * int(x[0]) for x in v]),
                    'items': sorted([x[1] for x in v], reverse=True),
                }
                for k, v in group.items()
            }
        
        elif grouping == 'Item':
            for row in sorted(reader):
                total_items = row[header.index(grouping)]
                total_value = row[header.index('Quantity')]
                items = row[header.index('Item')]
                price = row[header.index('Price_in_gold')]
                group[total_items].append((total_value, items, price))
                
            group = {
                'group' + k: {
                    'total_items': sum([int(x[0]) for x in v]),
                    'total_value': sum([int(x[2]) * int(x[0]) for x in v]),
                    'items': sorted([x[1] for x in v], reverse=True),
                }
                for k, v in group.items()
            }           
        
        if sum(x['total_items'] for x in group.values()) != secret_key:
            group.clear()
            group = {"error": "access denied"}

        json.dump(group, j_f, indent=3)


process_treasures('treasure.csv', 'result.json', 42, 'Item')j