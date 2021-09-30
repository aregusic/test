price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1

elif has_good_credit == False:
    down_payment = price * 0.2

print(f"down payment: {down_payment}")
