class GalaxyGuideError(Exception):
    pass


class PageNotFoundError(GalaxyGuideError):
    pass


class BabbleFishError(GalaxyGuideError):
    pass


class InvalidCoordinatesError(GalaxyGuideError):
    pass


def search_planet(guide, planet_name, coordinates):
    if planet_name not in guide:
        raise PageNotFoundError(f"Страница о планете '{planet_name}' не найдена в путеводителе.")
    
    if coordinates != guide[planet_name][1]:
        raise InvalidCoordinatesError(f"Неверные координаты для планеты '{planet_name}'. Ожидалось {guide[planet_name][1]}, получено {coordinates}")
    
    if (guide[planet_name][0] == '') or (guide[planet_name][0] == None):
        raise BabbleFishError(f"Не удалось перевести описание планеты '{planet_name}': язык не распознан.")
    
    return f"Описание планеты {planet_name}: {guide[planet_name][0]}"


guide = {
    "Магратея": ("Удивительная планета, где горы парят в воздухе.", (10, 20)),
    "Бетельгейзе": ("", (5, 15)),  # пустое описание
    "Арктур": (None, (0, 0))  # описание отсутствует
}

try:
    search_planet(guide, "Бетельгейзе", (5, 15))  # BabbleFishError
except Exception as e:
    print(e)
try:
    search_planet(guide, "Арктур", (0, 0))  # BabbleFishError
except Exception as e:
    print(e)