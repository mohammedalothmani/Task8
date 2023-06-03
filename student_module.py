class Student:
    def __init__(self, name, age, city,):
        self.name = name
        self.age = age
        self.city = city
        self.marks = []
    def add_mark(self, mark):
        self.marks.append(mark)

    def all_marks(self):
        return self.marks

    def calc_aver(self,):
        if not self.marks:
            return 'add marks'
        else:
            averg = sum(self.marks) / len(self.marks)
            print(f'the student {self.name} has {self.age} years old and live in {self.city} city , have Average {averg} '
                  f'for his marks {self.marks}')
            return












