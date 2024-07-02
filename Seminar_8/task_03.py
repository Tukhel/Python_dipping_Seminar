# Задание №3.
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import json
import csv
from pathlib import Path


def json_2_csv(path: Path | str, ) -> None:
    with (
        open(path, 'r', encoding='utf-8') as f_read,
        open(path.stem + '.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        data = json.load(f_read)
        rows = []
        for level, id_name in data.items():
            for _id, name in id_name.items():
                rows.append({'level': level, 'id': _id, 'name': name})

        csv_writer = csv.DictWriter(
            f_write,
            fieldnames=['level', 'id', 'name'],
            dialect='excel',
            quoting=csv.QUOTE_NONNUMERIC
        )
        csv_writer.writeheader()
        csv_writer.writerows(rows)


if __name__ == '__main__':
    json_2_csv(
        Path(r'D:\Education\Python\Dipping\Seminars\Seminar_8\users.json'))
