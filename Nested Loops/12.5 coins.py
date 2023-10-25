
change = float(input())
total_coins_count = 0

while True:
    if change // 2 > 0:
        two_lv_coins_count = change // 2
        total_coins_count += two_lv_coins_count
        change = (change % 2)
        change = "{:.2f}".format(change)
        change = float(change)
    elif change // 1 > 0:
        one_lv_coins_count = change // 1
        total_coins_count += one_lv_coins_count
        change = change % 1
        change = "{:.2f}".format(change)
        change = float(change)
    elif change // 0.5 > 0:
        fifty_st_coin = change // 0.5
        total_coins_count += fifty_st_coin
        change = change % 0.5
        change = "{:.2f}".format(change)
        change = float(change)
    elif change // 0.2 > 0:
        twenty_st_coin = change // 0.2
        total_coins_count += twenty_st_coin
        change = change % 0.2
        change = "{:.2f}".format(change)
        change = float(change)
    elif change // 0.1 > 0:
        one_st_coin = change // 0.1
        total_coins_count += one_st_coin
        change = change % 0.1
        change = "{:.2f}".format(change)
        change = float(change)
    elif change // 0.05 > 0:
        one_st_coin = change // 0.05
        total_coins_count += one_st_coin
        change = change % 0.05
        change = "{:.2f}".format(change)
        change = float(change)
    elif change // 0.02 > 0:
        one_st_coin = change // 0.02
        total_coins_count += one_st_coin
        change = change % 0.02
        change = "{:.2f}".format(change)
        change = float(change)
    elif change // 0.01 > 0:
        one_st_coin = change // 0.01
        total_coins_count += one_st_coin
        change = change % 0.01
        change = "{:.2f}".format(change)
        change = float(change)
    if change == 0:
        break
print(int(total_coins_count))