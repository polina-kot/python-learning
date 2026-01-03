# TODO Напишите функцию find_common_participant

def find_common_participants(participants1, participants2, separator=","):
    list1 = participants1.split(separator)
    list2 = participants2.split(separator)
    set1 = set(list1)
    set2 = set(list2)

    common_set = set1.intersection(set2)
    common_list = sorted(list(common_set))
    return common_list

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"


print("Тест 1 (разделитель по умолчанию - запятая):")
result1 = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {result1}")
print()

participants_first_group_spaces = "Иванов Петров Сидоров"
participants_second_group_spaces = "Петров Сидоров Смирнов"
print("Тест 2 (разделитель - пробел):")
result2 = find_common_participants(participants_first_group_spaces,
                                   participants_second_group_spaces,
                                   separator=" ")
print(f"Общие участники: {result2}")
print()

participants_first_group_semicolon = "Иванов;Петров;Сидоров"
participants_second_group_semicolon = "Петров;Сидоров;Смирнов"
print("Тест 3 (разделитель - точка с запятой):")
result3 = find_common_participants(participants_first_group_semicolon,
                                   participants_second_group_semicolon,
                                   separator=";")
print(f"Общие участники: {result3}")
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
