#python3
import sys

def money_change_greedy_util(money, coins):
    count = 0

    for coin in coins:
        if(money <= 0):
            break
        if(money >= coin):
            count += money // coin
            money = money % coin

    return count
def money_change_greedy(money):
    return money_change_greedy_util(money, (4,3,1))

def money_change_rec_util(money, coins):
    if(money == 0):
        return 0
    
    min_coins = 9999999999
    for coin in coins:
        if(money >= coin):
            num_coins = money_change_rec_util(money - coin, coins) + 1
            if(num_coins < min_coins):
                min_coins = num_coins
    
    return min_coins
def money_change_rec(money):
    return money_change_rec_util(money, (4,3,1))

def money_change_dynamic_util(money, coins):
    if(money <= 0):
        return 0
    min_coins = [0] + [9999999999]*money
    for i in range(1, money+1):
        for coin in coins:
            if(i >= coin):
                temp_coin = min_coins[i-coin]+1
                if(temp_coin < min_coins[i]):
                    min_coins[i] = temp_coin
    
    return min_coins[money]
def money_change_dynamic(money):
    return money_change_dynamic_util(money, (1,3,4))

if __name__ == "__main__":
    
    # test trigger
    if(len(sys.argv) == 2):
        if(sys.argv[1] == '-t'):
            from Stress_Test import Test
            test = Test(test_func = money_change_rec,
                        solution_func = money_change_dynamic,
                        iterations = 100)
            test.run()
    else:
        size = int(input())
        print("{}".format(money_change_dynamic(size)))

'''
2

34

'''