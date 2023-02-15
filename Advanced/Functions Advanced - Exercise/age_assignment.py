#8. Age Assignment
#Create a function called age_assignment() that receives a different number of names and a different number of key-value pairs. 
#The key will be a single letter (the first letter of each name) and the value - a number (age). 
#Find its first letter in the key-value pairs for each name and assign the age to the person's name.
#Then, sort the names in ascending order (alphabetically) and return the information for each person on a new line in the format: "{name} is {age} years old."

def age_assignment(*names, **data):
    result = []

    for letter, age in data.items():
        person_name = ""

        for name in names:
            if name.startswith(letter):
                person_name = name
                break

        result.append(f"{person_name} is {age} years old.")

    return '\n'.join(sorted(result))
