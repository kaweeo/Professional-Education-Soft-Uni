def pos_neg_separator(*nums):
    total_sum_pos = sum(num for num in nums if num > 0)
    total_sum_negative = sum(num for num in nums if num < 0)
    print(total_sum_negative)
    print(total_sum_pos)
    if total_sum_pos - abs(total_sum_negative) > 0:
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")

pos_neg_separator(*map(int, input().split()))