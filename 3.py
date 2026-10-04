def potions(line: str):
    result = []
    with open('recipes.txt', 'r', encoding='utf-8') as recipes:
        recipes = [x.rstrip().split(',') for x in recipes.readlines()]
        for r in recipes:
            if line.lower() in r[0]:
                result.append(r[1:])
        return result[-1]
        
print(potions('Ти'))