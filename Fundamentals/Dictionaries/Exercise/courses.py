#8. Courses

#Write a program that keeps the information about courses. Each course has a name and registered students.

#You will be receiving a course name and a student name until you receive the command "end".

#You should register each user into the corresponding course. If the given course does not exist, add it.

#When you receive the command "end", print the courses with their names and total registered users. For each course, print the registered users.

commands = input()
courses = dict()
while commands != "end":
    commands = commands.split(" : ")
    course_name = commands[0]
    student_name = commands[1]
    if course_name not in courses.keys():
        courses[course_name] = list()
    courses[course_name].append(student_name)

    commands = input()
for course, list_of_student in courses.items():
    count_of_students = len(list_of_student)
    print(f"{course}: {count_of_students}")
    for student in list_of_student:
        print(f"-- {student}")
