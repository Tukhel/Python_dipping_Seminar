# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли
# для сортировки.
import os

import generator_files as gf
from pathlib import Path


def sort_files(path: str | Path, groups: dict[Path, list[str]] = None) -> None:
    if groups is None:
        groups = {
            Path('videos'): list(['avi', 'mkv']),
            Path('pictures'): list(['png', 'jpeg']),
            Path('music'): list(['mp3'])
        }

    if isinstance(path, str):
        path = Path(path)

    os.chdir(path)
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for files in list(os.walk(Path.cwd()))[0][-1]:
            if files.split('.')[-1] in ext_list:
                os.replace(files, os.path.join(target_dir, files))


path_files = r'D:\Education\Python\Dipping\Seminars\Seminar_7\S7\test'
# gf.gen_files(path_files, avi=2, mkv=3, png=1, jpeg=1, mp3=3, txt=2)
sort_files(path_files)
