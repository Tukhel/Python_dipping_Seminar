# Напишите функцию, которая принимает на вход строку -
# абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.
def get_file_info(in_file_path):
    file_name = in_file_path.split('/')[-1]
    file_extension = file_name.split('.')[-1]
    path = in_file_path[:-len(file_name)]
    res = (path, file_name[:-len(file_extension)-1], '/' + file_extension)
    return res


file_path = 'C:/Users/User/Documents/example.txt'
print(get_file_info(file_path))
