#5. Emoticon Finder

#Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol. The input will be provided as a single string.

import re

text = input()
emoji_occurrences_indices = [_.start() for _ in re.finditer(r":", text)]
for emoji in emoji_occurrences_indices:
    print(f"{text[emoji]}{text[emoji + 1]}")
