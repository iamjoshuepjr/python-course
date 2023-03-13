students = [
    {'name': 'Joshuép Jr.' , 'age': 24, 'gpa': 4.5},
    {'name': 'Aurora'      , 'age': 21, 'gpa': 4.0},
    {'name': 'Carla'       , 'age': 18, 'gpa': 3.5}
]
i = 1
for student in students:
    print(f"Student [{i}]" + 
          f"\nName: {student['name']}" + 
          f"\nAge: {student['age']}" + 
          f"\nGPA: {student['gpa']}")
    i+=1

school = {
    'students': students,
    'teachers': [
        {'name': 'Martha' , 'class': 'Bachelor Degree'},
        {'name': 'Adriana', 'class': 'Master Degree'},
        {'name': 'Juli'   , 'class': 'PhD'}
    ]
} 
i = 1
for student in school['students']:
    print(f"Student [{i}]" + 
          f"\nName: {student['name']}" + 
          f"\nAge: {student['age']}" + 
          f"\nGPA: {student['gpa']}")
    i+=1

i = 1
for teacher in school['teachers']:
    print(f"Teacher [{i}]" + 
          f"\nName: {teacher['name']}" + 
          f"\nClass: {teacher['class']}")
    i+=1