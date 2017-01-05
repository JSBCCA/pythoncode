coins = {"1p": 1,
         "2p": 2,
         "5p": 5,
         "10p": 10,
         "20p": 20,
         "50p": 50,
         "£1": 100,
         "£2": 200}


def combo_if(num_of_coin, coin_value, coin_name):
    if coin_value * num_of_coin == 200:
        print(str(num_of_coin) + "×" + coin_name)


def combos(max_num_of_coin, coin_value, coin_name):
    for num_of_coin in range(max_num_of_coin, -1, -1):
        combo_if(num_of_coin, coin_value, coin_name)
        # add a new combo_if for previous coins plus current coin


def coin_combos():
    for coin_name in coins:
        coin_value = coins[coin_name]
        max_num_of_coin = int(200 / coin_value)
        combos(max_num_of_coin, coin_value, coin_name)


print()
coin_combos()
print()

# print all combinations that equal 200
