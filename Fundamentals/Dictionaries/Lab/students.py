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
