#10. *Winning Ticket

#The lottery is exciting. However, checking a million tickets for winnings only by hand is not. So, you are given the task of creating a program that automatically checks if a ticket is a winner.

#You are given a collection of tickets separated by commas and spaces (one or many). You need to check each ticket to see if it has a winning combination of symbols:

#· A valid ticket has exactly 20 characters.

#· A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at least 6 times in both halves of the tickets.

#· In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides

#An example of a valid winning ticket:

#"Cash$$$$$$Ca$$$$$$sh"

An example of a Jackpot winning valid ticket:

"$$$$$$$$$$$$$$$$$$$$"

def match_symb(part):
    match_symbols = 0
    current_match_symbols = 0
    for i in range(10):
        if current_symbol == part[i]:
            current_match_symbols += 1
        else:
            current_match_symbols = 0
        if match_symbols < current_match_symbols:
            match_symbols = current_match_symbols
    return match_symbols


is_symbols_match = lambda symbols, ticket: [sym in ticket for sym in symbols]
tickets = input().split(",")
tickets = [ticket.strip() for ticket in tickets]
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        if not any(is_symbols_match(["@", "#", "$", "^"], ticket)):
            print(f'ticket "{ticket}" - no match')
        else:
            current_symbol = ["@", "#", "$", "^"][is_symbols_match(["@", "#", "$", "^"], ticket).index(True)]
            if current_symbol * 20 == ticket:
                print(f'ticket "{ticket}" - 10{current_symbol} Jackpot!')
            else:
                left_part = match_symb(ticket[0:10])
                right_part = match_symb(ticket[10:20])
                if left_part <= right_part:
                    match_symbols = left_part
                else:
                    match_symbols = right_part
                if match_symbols >= 6:
                    print(f'ticket "{ticket}" - {match_symbols}{current_symbol}')
                else:
                    print(f'ticket "{ticket}" - no match')
