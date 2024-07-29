class Archive:
    _instance = None

    def __new__(cls, text=None, number=None):
        if cls._instance is not None:
            if text is not None and number is not None:
                cls._instance.archive_text.append(text)
                cls._instance.archive_number.append(number)
            return cls._instance
        else:
            cls._instance = super(Archive, cls).__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
            return cls._instance

    def __init__(self, text=None, number=None):
        if text is not None and number is not None:
            self.text = text
            self.number = number

            if text not in self.archive_text and number not in self.archive_number:
                self.archive_text.append(text)
                self.archive_number.append(number)

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f"Archive({self.text!r}, {self.number!r})"


archive1 = Archive("First Text", 1)
print(archive1)

archive2 = Archive("Second Text", 2)
print(archive2)

archive3 = Archive("Third Text", 3)
print(archive3)
