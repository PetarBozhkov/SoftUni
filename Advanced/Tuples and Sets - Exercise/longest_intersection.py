#5. Longest Intersection
#Write a program that finds the longest intersection. You will be given a number N. 
#On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". 
#You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
#Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the format: 
#"Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
#Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.

longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [el.split(",") for el in input().split("-")]
    first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))
    intersection = first_range.intersection(second_range)

    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection

print(
    f"Longest intersection is "
    f"[{', '.join(str(x) for x in longest_intersection)}] "
    f"with length {len(longest_intersection)}"
)
