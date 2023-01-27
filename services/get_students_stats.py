from csv import DictReader


CONTESTS = [
    {
        'id': [45316],
        'name': 'Вывод данных',
    },
    {
        'id': [45344],
        'name': 'Ввод данных',
    },
    {
        'id': [45720],
        'name': 'Арифметические операции',
    }
]


def get_students(contests: list[dict]) -> dict:
    """Получение списка учащихся"""

    contests_counts = len(contests)
    students = dict()

    for contest in contests:
        contest_ids = contest['id']
        for contest_id in contest_ids:
            filename = f"standings/standings-{contest_id}.csv"
            try:
                with open(filename, 'r', encoding='utf8') as csvfile:
                    reader = DictReader(csvfile)
                    for row in reader:
                        name = row['user_name']
                        students |= {name: ['—'] * contests_counts}
            except FileNotFoundError:
                print(f"Не найден файл с результатами олимпиады {contest_id}.")

    return students


def update_results(students: dict, contests: list) -> dict:
    """Получить результаты темы"""

    for number, contest in enumerate(contests):
        contest_ids = contest['id']
        for contest_id in contest_ids:
            filename = f"standings/standings-{contest_id}.csv"
            try:
                with open(filename, 'r', encoding='utf8') as csvfile:
                    reader = DictReader(csvfile)
                    for row in reader:
                        name = row['user_name']
                        score = row['Score']
                        students[name][number] = score
            except FileNotFoundError:
                print(f"Не найден файл с результатами олимпиады {contest_id}.")

    return students


def main() -> None:
    students = get_students(CONTESTS)
    students = update_results(students, CONTESTS)
    print(students)


if __name__ == '__main__':
    main()
