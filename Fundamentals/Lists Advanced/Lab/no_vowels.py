text = input()
no_vowels = ['a', 'o', 'u', 'e', 'i']
result = [character for character in text if character.lower() not in no_vowels]
print(''.join(result))
