import csv

class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, str) or value.isalpha() or not value[0].isupper():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, "")

class Student:
    name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            subjects_list = next(reader)
            for subject in subjects_list:
                self.subjects[subject] = {
                    'grades': [],
                    'test_scores': []
                }

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        scores = self.subjects[subject]['test_scores']
        return sum(scores) / len(scores) if scores else 0

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects.values():
            total_grades.extend(subject['grades'])
        return (sum(total_grades) / len(total_grades)) if total_grades else 0

    def __str__(self):
        subjects_with_grades = [subject for subject, value in
                                self.subjects.items() if value['grades']]
        subjects_str = ", ".join(subjects_with_grades)
        return f"Студент: {self.name}\nПредметы: {subjects_str}"

# Пример использования
try:
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)

except ValueError as e:
    print(e)