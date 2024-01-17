text_input = input()

symbol_dict = {}

for symbol in text_input:
    if not symbol in symbol_dict.keys():
        symbol_dict[symbol] = 1
    else:
        symbol_dict[symbol] += 1

sorted_keys = sorted(symbol_dict.keys())

for key in sorted_keys:
    print(f"{key}: {symbol_dict[key]} time/s")



# text = input()
#
# for symbol in sorted(set(text)):
#     print(f"{symbol}: {text.count(symbol)} time/s")


# occurrences = {}
#
# for symbol in input():
#     occurrences[symbol] = occurrences.get(symbol, 0) + 1
#
# for symbol, times in sorted(occurrences.items()):  # (("a", 1), ("b", 3))
#     print(f"{symbol}: {times} time/s")
