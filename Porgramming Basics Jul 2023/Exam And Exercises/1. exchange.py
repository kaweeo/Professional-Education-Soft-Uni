
btc_bgn = 1168
yuan_dollar = 0.15
dollar_bgn = 1.76
euro_bgn = 1.95

btc_count = int(input())
yuan_count = float(input())
commission = float(input())

btc_tot = (btc_count * btc_bgn)   # 598.974358974 bgn
yuan_tot = yuan_count * yuan_dollar * dollar_bgn  # 1.32 bgn
tot_bgn = btc_tot + yuan_tot
tot_euro = tot_bgn / 1.95
total = tot_euro - (tot_euro * (commission / 100))
print(f"{total:.2f}")

