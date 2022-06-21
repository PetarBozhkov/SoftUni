# Решение на Иван Шопов
# deck_of_cards = input().split()
# number_of_shuffles = int(input())
# for shuffle in range(number_of_shuffles):
#    final_deck = []
#    middle_of_the_deck = len(deck_of_cards) // 2
#    left_part = deck_of_cards[0::middle_of_the_deck]
#    right_part = deck_of_cards[middle_of_the_deck::]
#    for index_of_cards in range(len(left_part)):
#        final_deck.append(left_part[index_of_cards])
#        final_deck.append(right_part[index_of_cards])
#    deck_of_cards = final_deck
# print(deck_of_cards)

string_of_card = input().split(' ')
count_of_shuffles = int(input())
half = int(len(string_of_card)/2)
for i in range(count_of_shuffles):
    left_half = string_of_card[:half]
    right_half = string_of_card[half:]
    string_of_card.clear()
    for i in range(half):
        string_of_card.append(left_half[i])
        string_of_card.append(right_half[i])
print(string_of_card)