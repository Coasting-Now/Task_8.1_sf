import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0 # задаём счётчик попыток
    predict_ltt = np.random.randint(1, 101) # предполагаемое число

    predict_cap = 101 # задаём верхнюю и нижнюю границу диапазона
    predict_bottom = 1

    while True:
        count += 1

        if predict_ltt < number: # если предполагаемое число меньше загаданного поднимаем нижнюю границу, сужаем диапазон
            predict_bottom = predict_ltt
            predict_ltt = (predict_cap + predict_bottom) // 2 # назначаем число в середине диапазона предполагаемым, "отсекая" из поиска в следующем цикле одну из половин чисел
            continue
        elif predict_ltt > number: # если предполагаемое число больше загаданного снижаем верхнюю границу, сужаем диапазон
            predict_cap = predict_ltt
            predict_ltt = (predict_cap + predict_bottom) // 2 # назначаем число в середине диапазона предполагаемым, "отсекая" из поиска в следующем цикле одну из половин чисел
            continue
        else:
            break
    
    # Ваш код заканчивается здесь

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)