# Задание №4.
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр _id на семь

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return self.__age


class Employees(Person):
    def __init__(self, first_name, last_name, age, id_num='000001', *args,
                 **kwargs):
        super().__init__(first_name, last_name, age)
        self._id = id_num
        self.access_level = sum(int(i) for i in str(self._id)) % 7

    def get_id(self):
        return self._id

    def get_level(self):
        return self.access_level


if __name__ == '__main__':
    w1 = Employees('Andrey', 'Tukhel', 34)
    print(w1.full_name())
    print(w1.get_id())
    print(w1.get_level())

    w2 = Employees('Ivan', 'Ivanov', 34, '025302')
    print(w2.full_name())
    print(w2.get_id())
    print(w2.get_level())
