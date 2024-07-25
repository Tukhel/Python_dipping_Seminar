# Задание №4.
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.
class Archive:
    num_arch = []
    text_arch = []

    def __init__(self, number, text):
        self.number = number
        self.text = text
        self.num_arch.append(number)
        self.text_arch.append(text)

    def __str__(self):
        """Method str"""
        return (f'{self.number = }\n{self.text = }\n{self.text_arch = }\n'
                f'{self.num_arch = }')

    def __repr__(self):
        """Method repr"""
        return f'{self.num_arch = }\n{self.text_arch = }'


a = Archive(5, 'Hello')
b = Archive(2, 'Hi')
print(a)
print(repr(b))
