def min_flips(coins):
    num_flips = 0  # Счетчик количества переворотов
    first_coin = coins[0]  # Запоминаем состояние первой монетки

    for coin in coins[1:]:
        if coin != first_coin:
            # Если текущая монетка отличается от первой, добавляем ее в счетчик
            num_flips += 1

    return num_flips

# Пример использования функции
coins = "TTHHTTHHHTTTH"  # Пример строки с состояниями монеток
result = min_flips(coins)
print("Минимальное количество переворотов: ", result)