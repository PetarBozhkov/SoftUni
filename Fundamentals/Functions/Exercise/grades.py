def type_of_grade(grade):
    result = None
    if 2 <= grade <= 2.99:
        result = 'Fail'
    elif 3 <= grade <= 3.49:
        result = 'Poor'
    elif 3.50 <= grade <= 4.49:
        result = 'Good'
    elif 4.50 <= grade <= 5.49:
        result = 'Very Good'
    elif 5.49 <= grade <= 6:
        result = 'Excellent'
    return result


score = float(input())
print(type_of_grade(score))

# my own solution
# grade = float(input())
#
# if 2.00 <= grade <= 2.99:
#    print("Fail")
# elif 3.00 <= grade <= 3.49:
#    print("Poor")
# elif 3.50 <= grade <= 4.49:
#    print("Good")
# elif 4.50 <= grade <= 5.49:
#    print("Very Good")
# else:
#    print("Excellent")


