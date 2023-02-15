#11. *Math Operations
#Write a function named math_operations that receives a different number of floats as arguments and 4 keyword arguments. 
#The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
#You need to take each float argument from the sequence and do mathematical operations as follows:
#· The first element should be added to the value of the key "a"
#· The second element should be subtracted from the value of the key "s"
#· The third element should be divisor to the value of the key "d"
#· The fourth element should be multiplied by the value of the key "m"
#· Each result should replace the value of the corresponding key
#· You must repeat the same steps consecutively until you run out of numbers
#Beware: You cannot divide by 0. If the operation could throw an error, you should skip the operation and continue to the next one.
#After you finish calculating all numbers, sort the four elements by their values in descending order. 
#If two or more values are equal, sort them by their keys in ascending order (alphabetically).
#In the end, return each key-value pair in the format "{key}: {value}" on separate lines. Each value should be formatted to the first decimal point.
#For more clarifications, see the examples below.

def math_operations(*numbers, **kwargs):
    for i in range(len(numbers)):
        key = list(kwargs.keys())[i % 4]

        if key == "a":
            kwargs[key] += numbers[i]
        elif key == "s":
            kwargs[key] -= numbers[i]
        elif key == "d":
            if numbers[i] != 0:
                kwargs[key] /= numbers[i]
        elif key == "m":
            kwargs[key] *= numbers[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join(f"{k}: {v:.1f}" for k, v in kwargs)
