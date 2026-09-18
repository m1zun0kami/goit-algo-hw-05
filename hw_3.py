import sys


def parse_log_line(line: str) -> dict:
    """
    Парсує рядок логу.
    :param line: рядок логу
    :return: словник з ключами дати, часу, рівню, та повідомлення
    """
    parts = line.strip().split(' ', 3)
    return {'date': parts[0],
            'time': parts[1],
            'level': parts[2].upper(),
            'message': parts[3]
            }


def load_logs(file_path: str) -> list:
    """
    Завантажує та парсує.
    :param file_path: шлях до файлу з логами
    :return: список словників
    """
    logs = []
    with open(file_path, 'r', encoding='utf-8') as fh:
        for log_str in fh:
            logs.append(parse_log_line(log_str))
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує записи за рівнем.
    :param logs: список логів
    :param level: рівень логу
    :return: фільтрований список логів
    """
    return list(filter(lambda log: log['level'] == level.upper(), logs))
    # return [log for log in logs if log['level'] == level.upper()]  - те саме через list comprehension


def count_logs_by_level(logs: list) -> dict:
    """
    Рахує кількість записів для кожного рівня.
    :param logs: список логів
    :return: словник за рівнем логів
    """
    counts = {}
    for log in logs:
        level = log['level']

        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1

    return counts


def display_log_counts(counts: dict):
    """
    Виводить таблицю статистики в консоль.
    :param counts: словник за кількістю логів певного рівня
    """
    print(f"Рівень логування | Кількість\n{'-' * 17}|{'-' * 10}")
    for level, count in counts.items():
        print(f'{level:<17}|{count}')


def main() -> None:
    """
    Отримує аргументи, завантажує логи, виводить статистику та деталі за рівнем.
    """
    file_path = sys.argv[1]
    try:
        logs = load_logs(file_path)
        display_log_counts(count_logs_by_level(logs))
        if len(sys.argv) > 2:
            level = sys.argv[2].upper()
            logs = filter_logs_by_level(logs, level)
            print(f"\nДеталі для логів рівня {level}:")

            for log in logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
    except FileNotFoundError:
        print('Файл не знайдено')
        return


if __name__ == '__main__':
    main()