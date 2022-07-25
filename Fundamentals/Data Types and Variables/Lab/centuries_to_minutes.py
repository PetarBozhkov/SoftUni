#4. Centuries to Minutes

#Write a program that reads an integer number of centuries and converts it to years, days, hours, and minute

centuries = int(input())

years = 100 * centuries
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60


print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
