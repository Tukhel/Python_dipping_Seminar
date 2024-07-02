# Задание №1.
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдоименами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json
from pathlib import Path


def convert_to_JSON(file: str | Path) -> None:
    data_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            data_dict[name.title()] = float(number)
    with open(file.stem + '.json', 'w', encoding='utf-8') as fj:
        json.dump(data_dict, fj, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    convert_to_JSON(
        Path(r'D:\Education\Python\Dipping\Seminars\Seminar_7\results.txt'))
