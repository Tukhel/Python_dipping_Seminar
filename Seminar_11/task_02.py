# Задание №2.
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

# Добавьте к задачам 1 и 2 строки документации для классов.

class Archive:
    """Класс архив. Добавление значений в список"""
    _instance = None

    def __new__(cls, num, string):
        """Метод new"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.arch_texts = []
            cls._instance.arch_nums = []
        else:
            cls._instance.arch_texts.append(cls._instance.string)
            cls._instance.arch_nums.append(cls._instance.num)
        return cls._instance

    def __init__(self, num, string):
        """Метод init"""
        self.num = num
        self.string = string


if __name__ == '__main__':
    a = Archive(5, 'Hello')
    b = Archive(2, 'Hi')
    c = Archive(3, 'Wats up')
    print(a.arch_texts, a.arch_nums)
    print(b.arch_texts, b.arch_nums)
    print(c.num)
    print(a.num)
    print(help(Archive))
    print(Archive.__doc__)
    print(Archive.__new__.__doc__)

# Альтернативный вариант
# class Archive:
#     num_arch = []
#     text_arch = []
#
#     def __init__(self, number, text):
#         self.number = number
#         self.text = text
#         self.num_arch.append(number)
#         self.text_arch.append(text)
#
#
# a = Archive(5, 'Hello')
# b = Archive(2, 'Hi')
# print(b.num_arch, b.text_arch)
# print(Archive.num_arch, Archive.text_arch)
