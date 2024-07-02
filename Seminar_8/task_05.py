# Задание №5.
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import pickle
from pathlib import Path
import json

def json_2_pickle(directory: Path | str):
    for file in directory.iterdir():
        if file.suffix == '.json':
            with (
                open(file, 'r', encoding='utf-8') as f_read,
                open(f'{file.stem}.pickle', 'wb') as f_write
            ):
                res = json.load(f_read)
                pickle.dump(res, f_write)


if __name__ == '__main__':
    json_2_pickle(Path(r'D:\Education\Python\Dipping\Seminars\Seminar_8'))