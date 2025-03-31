from error import StudentLimitError

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