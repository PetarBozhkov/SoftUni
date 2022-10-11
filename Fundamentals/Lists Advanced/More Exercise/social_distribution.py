#1. Social Distribution
#A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what, and that is exactly what you are called to do for this problem.
#On the first line, you will be given the population (numbers separated by comma and space ", "). 
#On the second line, you will be given the minimum wealth. 
#You should distribute the wealth so that no part of the population has less than the minimum wealth. 
#To do that, you should always take wealth from the wealthiest part of the population.
#There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible".

def poor_rich(possessions: list, wealth: int):
    for index in range(len(possessions)):
        if possessions[index] < wealth:
            min_wealth_index = possessions.index(min(possessions))
            max_wealth_index = possessions.index(max(possessions))
            if possessions[max_wealth_index] > possessions[min_wealth_index]:
                difference = wealth - possessions[min_wealth_index]
                possessions[min_wealth_index] += difference
                possessions[max_wealth_index] -= difference
    if min(possessions) == wealth:
        return True, possessions
    else:
        return False


population = list(map(int, input().split(', ')))
minimum_wealth = int(input())
if poor_rich(population, minimum_wealth):
    print(population)
else:
    print("No equal distribution possible")
