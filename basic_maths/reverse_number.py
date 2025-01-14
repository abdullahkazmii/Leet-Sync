def reverse_number(x):
    rev_number = 0
    is_negative = x < 0
    x = abs(x)

    while x > 0:
        last = x % 10
        rev_number = (rev_number * 10) + last
        x = x // 10

    if is_negative:
        rev_number = -rev_number

    if rev_number < -(2**31) or rev_number > (2**31 - 1):
        return 0

    print(rev_number)


reverse_number(-3120)
