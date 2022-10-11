#2. Take/Skip Rope
#Write a program, which reads a string and skips through it, extracting a hidden message. The algorithm you should implement is as follows:
#Let us take the string "skipTest_String044160" as an example.
#Take every digit from the string and transfer it somewhere. 
#After this operation, you should have two lists of items - a numbers list and a non-numbers list:
#· Numbers' list: [0, 4, 4, 1, 6, 0]
#· Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
#After that, take every digit in the numbers list and split it up into a take list and a skip list. In the take list, you should keep all digits at an even index. In the skip list, you should keep all digits at an odd index.
#· Numbers' list: [0, 4, 4, 1, 6, 0]
#· Take list: [0, 4, 6]
#· Skip list: [4, 1, 0]
#Afterward, iterate over both lists:
#· First, take m characters from the non-numbers list and store it in a result string
#· Then, skip n characters from the non-numbers list
#Note that the skipped characters are summed up as they go. The process would look like this:
#1. Current string: "skipTest_String". Take 0 characters and skip 4 characters:
#· Taken string: ""
#· Skipped string: "skip"
#2. The remaining string looks like this: "Test_String". Take 4 characters and skip 1 character:
#· Taken string: "Test"
#· Skipped string: "_"
#3. The string looks like this: "String". Take 6 characters and skip 0 characters:
#· Taken string: "String"
#· Skipped string: ""
#4. The final string is "TestString".
#After that, print the final string on the console.

line = list(map(str, input()))
numbers = list()
non_number = list()
for i in range(len(line)):
    if line[i].isdigit():
        numbers.append(line[i])
    else:
        non_number.append(line[i])
numbers = list(map(int, numbers))
take_list = [numbers[number] for number in range(len(numbers)) if number % 2 == 0]
pass_list = [numbers[number] for number in range(len(numbers)) if number % 2 != 0]
result = list()
index = 0
while non_number:
    if take_list and pass_list:
        if index % 2 == 0:
            for i in range(take_list.pop(0)):
                if non_number:
                    result.append(non_number[0])
                    non_number.pop(0)
        else:
            for i in range(pass_list.pop(0)):
                if non_number:
                    non_number.pop(0)
        index += 1
    else:
        break
final_result = "".join(result)
print(final_result)
