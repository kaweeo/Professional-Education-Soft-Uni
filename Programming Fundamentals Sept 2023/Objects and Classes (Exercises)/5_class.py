class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []  # Initialize an empty list for students
        self.grades = []    # Initialize an empty list for grades

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0  # Avoid division by zero if there are no grades
        average_grade = sum(self.grades) / len(self.grades)
        return average_grade

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)