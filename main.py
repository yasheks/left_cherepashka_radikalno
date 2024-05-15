# Запрашиваем у пользователя высоту и ширину карты
height = int(input("Введите высоту карты: "))
width = int(input("Введите ширину карты: "))

# Создаем пустой двумерный массив для карты
map_array = [['С' for _ in range(width)] for _ in range(height)]

# Запрашиваем у пользователя данные для заполнения карты
for i in range(height):
    for j in range(width):
        cell_data = input(f"Введите данные для клетки ({i}, {j}) на карте (С-свободная, З-занято, П-персонаж): ")
        map_array[i][j] = cell_data

# Выводим карту
for row in map_array:
    print(' '.join(row))