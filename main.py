def move(start_x, start_y, map):
    global map_array
    if start_x + 1 < len(map) and map[start_x + 1][start_y] == 'С':
        map_array[start_x + 1][start_y] = "Ч"
        map_array[start_x][start_y] = "С"
        for row in map_array:
            print(' '.join(row))
        print(' ')
        return move(start_x + 1, start_y, map)

    if start_x - 1 >= 0 and map[start_x - 1][start_y] == 'С':
        map_array[start_x - 1][start_y] = "Ч"
        map_array[start_x][start_y] = "С"
        for row in map_array:
            print(' '.join(row))
        print(' ')
        return move(start_x - 1, start_y, map)

    if start_y + 1 < len(map[0]) and map[start_x][start_y + 1] == 'С':
        map_array[start_x][start_y + 1] = "Ч"
        map_array[start_x][start_y] = "С"
        for row in map_array:
            print(' '.join(row))
        print(' ')
        return move(start_x, start_y + 1, map)

    if start_y - 1 >= 0 and map[start_x][start_y - 1] == 'С':
        map_array[start_x][start_y - 1] = "Ч"
        map_array[start_x][start_y] = "С"
        for row in map_array:
            print(' '.join(row))
        print(' ')
        return move(start_x, start_y - 1, map)

height = int(input("Введите высоту карты: "))
width = int(input("Введите ширину карты:"))

map_array = [['С' for _ in range(width)] for _ in range(height)]

for i in range(height):
    for j in range(width):
        cell_data = input(f"Введите данные для клетки ({i}, {j}) на карте (С-свободная, З-занято, Ч-Черепашка): ").upper()
        if cell_data == "Ч":
            start_x = i
            start_y = j
        map_array[i][j] = cell_data
print("Ваша карта:")
for row in map_array:
    print(' '.join(row))
print("Передвижение черепахи:")
move(start_x, start_y, map_array)

