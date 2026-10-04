import pandas as pd
from openpyxl import load_workbook

file_path = "census.xlsx"
df = pd.read_excel(file_path)

m_d = max(
    [(int(x), [x for x in df["Раса"]].count(x)) for x in df["Раса"]]
)[1]

wb = load_workbook("census.xlsx")
ws = wb.create_sheet("Статистика")

ws["A1"] = "Максимальный возраст"
ws["B1"] = max([int(x) for x in df["Возраст"]])
ws["A2"] = "Средний возраст"
ws["B2"] = round(sum([int(x) for x in df["Возраст"]]) / len([x for x in df["Возраст"]]), 2)
ws["A3"] = "Максимальный рост"
ws["B3"] = max([int(x) for x in df["Рост"]])
ws["A4"] = "Средний рост"
ws["B4"] = round(sum([int(x) for x in df["Рост"]]) / len([x for x in df["Рост"]]),2)
ws["A5"] = "Титульная раса (код)"
ws["B5"] = m_d
ws["A6"] = "Процент титульной расы"
ws["B6"] = round((max([(int(x), [x for x in df["Раса"]].count(x))for x in df["Раса"]])[0] / len([x for x in df["Раса"]])) * 100, 2)

wb.save("statistics.xlsx")