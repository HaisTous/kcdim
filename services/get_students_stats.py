from csv import DictReader
from datetime import datetime

CONTESTS = [
    {
        'id': (45316,),
        'name': 'Вывод данных',
        'href': 'topics/data-output.html',
    },
    {
        'id': (45344,),
        'name': 'Ввод данных',
        'href': 'topics/data-input.html',
    },
    {
        'id': (45720, 45855),
        'name': 'Арифметические операции',
        'href': 'topics/arithmetic.html',
    },
    {
        'id': (46059, 46125),
        'name': 'Условный оператор',
        'href': 'topics/condition.html',
    },
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
                        students[name][number] = int(students[name][number]) + int(score)
            except FileNotFoundError:
                print(f"Не найден файл с результатами олимпиады {contest_id}.")

    return students


def generate_html(students: dict) -> str:
    """Генерация html-файла со списком учащихся"""

    current_datetime = datetime.now()
    date = str(current_datetime)[:16]

    html = f'<main>\n<h2 class="title">Список учащихся</h2>\n' \
           f'<p class="updated_date">Последнее обновление: {date}</p>\n' \
           f'<div class="stripped-table">\n' \
           f'<table>\n<thead>\n<tr>\n<th scope="col">#</th>\n' \
           f'<th scope="col" class="text-left">Учащийся</th>\n' \

    for number, contest in enumerate(CONTESTS):
        html += f'<th scope="col">\n' \
                f'<a href="{contest["href"]}" class="tooltip group">{number + 1}\n' \
                f'<span class="tooltiptext group-hover:visible group-hover:opacity-100">{contest["name"]}</span>\n' \
                f'</a>\n</th>\n'

    html += f'<th scope="col">Всего</th>\n</tr>\n</thead>\n<tbody>'

    for number, student in enumerate(students):
        html += f'<tr>\n<td>{number + 1}</td>\n' \
                f'<th scope="row" class="name">{student}</th>\n'
        for score in students[student]:
            html += f'<td>{score}</td>\n'
        html += f'<td>{sum(map(int, students[student]))}</td>\n'
    html += '</tbody>\n</table>\n</div>\n</main>'
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
