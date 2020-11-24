# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

try:
    with open("text_hw_5_task_7.txt", encoding='utf-8') as f_obj:
        profit = {}
        profit_average = {}
        av_pr = 0
        i = 0
        for line in f_obj:
            profit_list = line.split()
            profit[profit_list[0]] = int(profit_list[2]) - int(profit_list[3])
            if int(profit_list[2]) > int(profit_list[3]):
                av_pr = av_pr + (int(profit_list[2]) - int(profit_list[3]))
                i += 1
        profit_average["average_profit"] = av_pr/i
        spisok_itog = [profit, profit_average]
        with open("json_hw_5_task_7.json", "w") as write_f:
            json.dump(spisok_itog, write_f)
except IOError:
    print("Произошла ошибка ввода-вывода!")