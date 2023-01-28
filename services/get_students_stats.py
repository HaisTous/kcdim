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
                    print(type(reader))
                    for row in reader:
                        name = row['user_name']
                        students |= {name: ['0'] * contests_counts}
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


def generate_html(students: dict) -> str:
    """Генерация html-файла со списком учащихся"""

    html = '<tbody>\n'
    for number, student in enumerate(students):
        html += f'<tr>\n<td>{number + 1}</td>\n' \
                f'<th scope="row" class="name">{student}</th>\n'
        for score in students[student]:
            html += f'<td>{score}</td>\n'
        html += f'<td>{sum(map(int, students[student]))}</td>\n'
    html += '</tbody>'
    return html


def write(text: str) -> None:
    """Запись текста в файл"""

    filename = f"standings/students.txt"
    with open(filename, "w", encoding='utf8') as file:
        file.write(text)


def main() -> None:
    students = get_students(CONTESTS)

    students = update_results(students, CONTESTS)
    students = dict(sorted(students.items(), key=lambda x: sum(map(int, x[1])), reverse=True))

    html = generate_html(students)
    write(html)


if __name__ == '__main__':
    main()
