currnet_sum = float(input())
currnet_sum = int(currnet_sum * 100)
coins_counter = 0

coins_counter += currnet_sum // 200
currnet_sum %= 200
coins_counter += currnet_sum // 100
currnet_sum %= 100
coins_counter += currnet_sum // 50
currnet_sum %= 50
coins_counter += currnet_sum // 20
currnet_sum %= 20
coins_counter += currnet_sum // 10
currnet_sum %= 10
coins_counter += currnet_sum // 5
currnet_sum %= 5
coins_counter += currnet_sum // 2
currnet_sum %= 2
coins_counter += currnet_sum // 1
currnet_sum %= 1

print(coins_counter)
