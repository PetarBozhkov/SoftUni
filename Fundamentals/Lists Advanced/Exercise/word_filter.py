words = input().split(' ')
filtered_words = [s for s in words if len(s) % 2 == 0]
print('\n'.join(filtered_words))
