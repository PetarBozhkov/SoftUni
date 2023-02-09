#4. Rectangle
#Create a function called rectangle(). It must have two parameters - length and width.
#First, you need to check if the given arguments are integers:
#· If one/ both of them is/ are NOT an integer/s, return the string "Enter valid values!"
#Create two inner functions:
#· area() - returns the area of the rectangle with the given length and width
#· perimeter() - returns the perimeter of the rectangle with the given length and width
#In the end, the rectangle function should return a string containing the area and the perimeter of a rectangle in the following format:
#"Rectangle area: {ract_area}
#Rectangle perimeter: {rect_perim}"

def rectangle(length, width):
    def rectangle_area():
        return length * width

    def rectangle_perimeter():
        return (length * 2) + (width * 2)

    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f'''Rectangle area: {rectangle_area()}
Rectangle perimeter: {rectangle_perimeter()}'''

print(rectangle(2, 10))
