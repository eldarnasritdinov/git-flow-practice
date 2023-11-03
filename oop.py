class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.diary = Diary(self)

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

class Diary:
    def __init__(self, student):
        self.student = student
        self.subjects = {}

    def add_subject(self, subject_name):
        subject = Subject(subject_name)
        self.subjects[subject_name] = subject

    def __str__(self):
        return f"Diary of {self.student.name}"

class Subject:
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def add_score(self, date, score):
        self.scores[date] = score

    def __str__(self):
        return f"Subject: {self.name}"

student1 = Student("Asyl", 18)
print(student1)

student1.diary.add_subject("Machine Learning")
student1.diary.add_subject("Fundamentals of System Engineering")
print(student1.diary)

math_subject = student1.diary.subjects["Machine Learning"]
math_subject.add_score("2023-11-01", 60)
math_subject.add_score("2023-11-10", 85)
print(math_subject.scores)

student2 = Student("Sanjar", 17)
print(student2)
print(student2.diary)
