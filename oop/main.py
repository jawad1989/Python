from typing import AsyncGenerator


class Student():
    def __init__(self, age, name, subjects, grades):
        self.age     = age
        self.name    = name
        self.subject = subjects
        self.grades  = grades
    
    def get_yob(self):
        return 2021 - self.age

    def get_grades(self):
        return self.grades

    def get_highest_grade(self):
        # max(self.grade, key=grades.get)
        sub    = list(self.grades.keys())
        scores = list(self.grades.values())
        return sub[scores.index(max(scores))]

subjects = ['maths','database','programming']
grades = {
    'maths': 80,
    'database': 85,
    'programming': 99
}
std = Student(15, 'Jawad', subjects, grades )
print("Year of Birth:", std.get_yob())

print("grades:", std.get_grades())

print( "Highest grade: ",std.get_highest_grade())