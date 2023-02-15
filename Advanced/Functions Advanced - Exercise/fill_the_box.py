#10. *Fill the Box
#Write a function called fill_the_box that receives a different number of arguments representing:
#· the height of a box
#· the length of a box
#· the width of a box
#· n-times a different number of cubes with exact size 1 x 1 x 1
#· a string "Finish"
#Your task is to fill the box with the given cubes until the current argument equals "Finish".

def fill_the_box(height, length, width, *cubes):
    space = height * length * width
    cubes = list(cubes)

    while cubes[0] != "Finish":
        space -= cubes.pop(0)

        if space < 0:
            cubes_left = sum([x for x in cubes if x != "Finish"])
            return f"No more free space! You have {cubes_left + abs(space)} more cubes."

    return f"There is free space in the box. You could put {space} more cubes."
