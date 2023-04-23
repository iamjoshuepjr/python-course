class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, academic_level):
        super().__init__(name, age)
        self.academic_level = academic_level

class Student(Person):
    def __init__(self, name, age, code):
        super().__init__(name, age)
        self.code = code

class Undergraduate(Student):
    def __init__(self, name, age, code, degree):
        super().__init__(name, age, code)
        self.degree = degree

undergraduate = Undergraduate('Joshuép Jr.', 24, 2499, 'Computer Science')
print(undergraduate.degree)