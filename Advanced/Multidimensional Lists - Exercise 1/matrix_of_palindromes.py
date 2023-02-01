#5. Matrix of Palindromes
#Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.
#· Rows define the first and the last letter: row 0 à 'a', row 1 à 'b', row 2 à 'c', …
#· Columns + rows define the middle letter:
#o column 0, row 0 à 'a', column 1, row 0 à 'b', column 2, row 0 à 'c', …
#o column 0, row 1 à 'b', column 1, row 1 à 'c', column 2, row 1 à 'd', …

rows, cols = [int(x) for x in input().split()]

start_end = ord('a')

for row in range(start_end, start_end + rows):
    for col in range(start_end, start_end + cols):
        print(f"{chr(row)}{chr((row + col) - start_end)}{chr(row)}", end=" ")

    print()
