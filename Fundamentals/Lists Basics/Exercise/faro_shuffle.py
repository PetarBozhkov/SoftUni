#5. Faro Shuffle

#A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. 
#Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.

#For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']

#Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made. 
#Print the state of the deck after the shuffle.

#Note: The length of the deck of cards will always be an even number.

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
