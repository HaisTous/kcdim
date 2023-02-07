import os
from pathlib import Path
from random import randint, uniform
from shutil import rmtree
from zipfile import ZipFile

NUMBER_OF_TESTS = 20
SAMPLES = ['1 1 1', '8 5 2', '11 5 4', '100000000 100000000 100000000']


def gen_input_data(number_of_tests: int, samples: list[str]) -> list[str]:
    """Генерация входных данных"""

    tests = samples[:]

    while len(tests) < number_of_tests:
        test = f""
        if test not in tests:
            tests.append(test)

    return tests


def gen_output_data(input_data: list[str]) -> list[str]:
    """Генерация выходных данных"""

    output_data = []
    for data in input_data:
        input_test = data.split()
        output_test = solution(input_test)
        output_data.append(output_test)

    return output_data


def solution(input_test: list[str]) -> str:
    """Решение задачи"""

    return f""


def delete_folder(folder_name: str) -> None:
    """Удаление папки"""

    if os.path.isdir(folder_name):
        rmtree(folder_name)


def create_folder(folder_name: str) -> None:
    """Создание папки """

    os.mkdir(folder_name)


def archive_folder(folder_name: str) -> None:
    """Архивация папки"""

    directory = Path(f"{folder_name}/")
    with ZipFile(f"{folder_name}.zip", mode="w") as archive:
        for file_path in directory.iterdir():
            archive.write(file_path, arcname=file_path.name)


def save_data(data: list[str], mode: str) -> None:
    """Сохранение данных в файл"""

    for i in range(len(data)):
        if i < 9:
            name = f"0{i + 1}"
        else:
            name = f"{i + 1}"

        if mode == "out":
            ext = ".a"
        else:
            ext = ""

        file_data = open(f"tests/{name}{ext}", "w", encoding="utf-8")
        file_data.write(data[i])


def main() -> None:
    delete_folder("tests")
    create_folder("tests")

    input_data = gen_input_data(NUMBER_OF_TESTS, SAMPLES)
    output_data = gen_output_data(input_data)
    save_data(input_data, "in")
    save_data(output_data, "out")

    archive_folder('tests')
    delete_folder("tests")


if __name__ == '__main__':
    main()
