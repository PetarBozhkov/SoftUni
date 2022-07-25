#6. Next Happy Year

#You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only distinct digits, for example, 2018. 
#Write a program that receives an integer number and finds the next happy year.

year = int(input())
happy_year_condition = False

while not happy_year_condition:
    year += 1
    set_year = set()

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_year_condition = len(set_year) == len(str(year))

print(year)
