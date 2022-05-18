# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#
# **Примеры строк файла:**
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# **Пример словаря:**
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import get_file_by_files_list as my_add_func
import re

science_dict = dict()

# ошибки здесь не обрабатываю. Введено не то - ну что ж
with open(my_add_func.get_file_by_current_folder(), "r") as reading_file:
    for line in reading_file:
        science_name, others = line.split(":")
        # только цифры
        num_sum = 0
        # воспользуемся регулярными выражениями. Нужны только цифры
        for num in ' '.join(re.split('[^\d]', others)).split():
            num_sum += my_add_func.get_number_by_string(num)
        science_dict[science_name] = num_sum
print(f"Final dict is {science_dict}")
