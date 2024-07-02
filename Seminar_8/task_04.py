# Задание №4.
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json
from pathlib import Path


def csv_2_json(path_csv: Path | str, path_json: Path | str) -> None:
    json_list = []
    with open(path_csv, 'r', encoding='utf-8') as f_read:
        csv_write = csv.reader(f_read)
        for i, line in enumerate(csv_write):
            if i != 0:
                json_dict = {}
                level, _id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = _id.rjust(10, '0')
                # json_dict['id'] = f'{int(_id):010}'
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f'{json_dict["name"]}'
                                         f'{json_dict["id"]}')
                json_list.append(json_dict)
    with open(path_json, 'w', encoding='utf-8') as f_write:
        json.dump(json_list, f_write, indent=4)


if __name__ == '__main__':
    csv_2_json(r'D:\Education\Python\Dipping\Seminars\Seminar_8\users.csv',
               r'D:\Education\Python\Dipping\Seminars\Seminar_8\New_users.json')
