#1. Data Types
#Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
#· If the data type is an int, multiply the number by 2.
#· If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
#· If the data type is a string, surround the input with "$".
#Print the result on the console.

def data_type(type: str, parametur):
    if type == 'int':
        return int(parametur) * 2
    elif type == 'real':
        return f'{float(parametur)*1.5:.2f}'
    elif type == 'string':
        return f'${parametur}$'


current_type = input()
current_paramentur = input()
print(data_type(type=current_type, parametur=current_paramentur))
