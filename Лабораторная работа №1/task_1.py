numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers2 = numbers[:4] + numbers[5:]
avg = round(sum(numbers2) / len(numbers), 2)


numbers[4] = avg

print("Измененный список:", numbers)
