#7. String Explosion

#Write a program that reads a string from the console that contains:

#· Explosions marked with '>'

#· Immediately after the mark, there will be an integer x, which signifies the strength of the explosion

#· Any other characters

#Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous explosion. You should not delete the explosion character – '>'
#When all characters are processed, print the final string.

text = input().split(">")
left_strength = 0
for word in text:
    for ch in range(len(word)):
        if word[ch].isdigit():
            current_word = ''
            strength = int(word[ch])
            if left_strength > 0:
                strength += left_strength
            if strength > len(word):
                left_strength += strength - len(word)
                strength = len(word)
            for i in range(strength):
                current_word = word[strength:]
            text[text.index(word)] = "".join(current_word)
output = ">".join(text)
print(output)
