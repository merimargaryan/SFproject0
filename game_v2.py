import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 50  # Начальное предполагаемое число
    low = 1  # Нижняя граница
    high = 100  # Верхняя граница

    while True:
        count += 1

        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            low = predict_number + 1
        else:
            high = predict_number - 1

        predict_number = (low + high) // 2  # Новое предполагаемое число

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
