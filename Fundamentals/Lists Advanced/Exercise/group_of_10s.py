numbers = list(map(int, input().split(", ")))
copy_numbers = numbers.copy()
group = 10

while len(numbers) > 0:
    tens = []
    for num in numbers:
        if num <= group:
            tens.append(num)
    print(f"Group of {group}'s: {tens}")
    for copy_num in tens:
        if copy_num in numbers:
            numbers.remove(copy_num)
    group += 10
