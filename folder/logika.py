has_high_income = True
has_good_credit = True
is_eligible_for_loan = False

if has_good_credit and has_high_income:         #moze i 'or'
    set(is_eligible_for_loan = True)            # if has_good_credit and not criminal record...
    print('Is eligible!')                                                #! provjerava jeli false,  ili true

else:
    print('Is not eligible!')

    # https://youtu.be/_uQrJ0TkZlc?t=4285