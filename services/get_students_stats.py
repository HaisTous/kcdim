import shutil
from csv import DictReader
from datetime import datetime as dt
import webbrowser
from time import sleep
import os

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
        'id': (46059, 46125, 46126, 46127),
        'name': 'Условный оператор',
        'href': 'topics/condition.html',
    },
    {
        'id': (46846, 46990),
        'name': 'Операторы цикла',
        'href': 'topics/loops.html',
    },
]


def download_contests(contests: list) -> None:
    """Скачивание результатов соревнований с Яндекс-Контеста"""

    for contest in contests:
        for ids in contest['id']:
            url = f"https://admin.contest.yandex.ru/api/contest/{ids}/monitor/csv"
            webbrowser.open(url)
            sleep(0.5)


def move_files(contests: list) -> None:
    """Перемещение контестов в папку с проектом"""

    src = os.path.expanduser('~') + '\\Desktop\\'
    dest = os.path.abspath(os.curdir) + '\\standings\\'

    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

    for contest in contests:
        for ids in contest['id']:
            filename = f'standings-{ids}.csv'
            shutil.move(src + filename, dest + filename)


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


def get_current_datetime() -> str:
    """Получение текущих даты и времени"""

    current_datetime = dt.now()
    datetime = str(current_datetime)[:16]

    months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    month_number = int(datetime[5:7])
    month = months[month_number]

    day = int(datetime[8:10])

    year = datetime[:4]

    time = datetime[11:]

    return f"{day} {month} {year} года в {time}"


def generate_data(students: dict) -> str:
    """Генерация html-файла со списком учащихся"""

    datetime = get_current_datetime()

    data = "data() {\n" \
           "return {\n"\
           f"date: '{datetime}',\n"

    data += f"topics: [\n"
    for number, contest in enumerate(CONTESTS):
        data += "{'id': " + f"{number + 1}, 'link': '{contest['href']}', 'name': '{contest['name']}'" + "},\n"
    data += f"],\n"

    data += f"students: [\n"
    for number, student in enumerate(students):
        data += "{'id': " + f"{number + 1}, 'name': '{student}', 'scores': ["
        for score in students[student]:
            data += f"{score},"
        data += f"], 'totalScore': {sum(map(int, students[student]))}" + '},\n'
    data += "],\n}\n},"

    return data


def write(text: str) -> None:
    """Запись текста в файл"""

    filename = f"standings/students.txt"
    with open(filename, "w", encoding='utf8') as file:
        file.write(text)


def main() -> None:
    download_contests(CONTESTS)
    move_files(CONTESTS)
    students = get_students(CONTESTS)

    students = update_results(students, CONTESTS)
    students = dict(sorted(students.items(), key=lambda x: sum(map(int, x[1])), reverse=True))

    data = generate_data(students)
    write(data)


if __name__ == '__main__':
    main()
