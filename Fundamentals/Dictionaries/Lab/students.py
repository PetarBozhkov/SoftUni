#4. Students

#You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}". 
#On the last line, you will receive a name of a course in snake case lowercase letters. 
#You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines.

#Note: each student's ID will always be unique

data = {}

while True:
    command = input()
    if ":" in command:
        tokens = command.split(":")
        name = tokens[0]
        id = int(tokens[1])
        course = tokens[2]
        if course not in data:
            data[course] = {}
        data[course][name] = id
    else:
        course = command.replace("_", " ")
        break

for k, v in data[course].items():
    print(f"{k} - {v}")
