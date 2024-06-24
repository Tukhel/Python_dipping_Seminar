from gropup_rename_files import rename_files
from Seminar_7.sort_files import sort_files
import Seminar_7.generator_files as gf

path_files = r'D:\Education\Python\Dipping\Seminars\Seminar_7\S7\test'
gf.gen_files(path_files, avi=2, mkv=3, png=1, jpeg=1, mp3=3, txt=2)
sort_files(path_files)
