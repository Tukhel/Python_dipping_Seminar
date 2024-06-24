# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
import os

from file_gen import file_gen
from pathlib import Path


def gen_files(path: str | Path, **kwargs) -> None:
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    os.chdir(path)
    for extent, count in kwargs.items():
        file_gen(extent=extent, file_count=count)


if __name__ == '__main__':
    gen_files(r'D:\Education\Python\Dipping\Seminars\Seminar_7\S7\test', txt=2,
              jpeg=1)
