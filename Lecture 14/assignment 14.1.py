class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}; Age: {self.age}; Gender: {self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}; Record book: {self.record_book}'

class StudentLimitError (Exception):
    pass

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise StudentLimitError ("Maximum group limit reached!")
        self.group.add(student)

    def delete_student(self, last_name):
        fifth_wheel = self.find_student(last_name)
        if fifth_wheel:
            self.group.remove(fifth_wheel)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\nStudents:\n{all_students} '

gr = Group('PD1')
try:
    for i in range(11):
        student = Student("Male", 20, f"TestStudent{i + 1}", f"LastName{i + 1}", f"AN{i + 1}")
        gr.add_student(student)
        print(f"Added: {student}")
except StudentLimitError as e:
    print(f"Error: {e}")
print(gr)