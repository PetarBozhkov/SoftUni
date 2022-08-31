#3. Match Dates
#Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". Use capturing groups in your regular expression.

import re
dates = input()
expression = r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
matches = re.finditer(expression, dates)
for match in matches:
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')
    print(f"Day: {day}, Month: {month}, Year: {year}")
