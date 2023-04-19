
# Input: [1, 1, 2, 0, -1, 3, 4, 4]


def result(list):
    uniq = set(list) # Создаем множество из списка
    return len(uniq) # Возвращаем количество уникальных чисел

# Пример использования
list = [1, 1, 2, 0, -1, 3, 4, 4]
total = result(list)
print("Количество уникальных чисел:", total)