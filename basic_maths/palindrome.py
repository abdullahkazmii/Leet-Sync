def isPalindrome(x: int) -> bool:
    rev_number = 0
    duplicate = x
    while x > 0:
        last = x % 10
        rev_number = (rev_number * 10) + last
        x = x // 10

    if rev_number == duplicate:
        print("True")
        return True

    else:
        print("False", rev_number)
        return False


isPalindrome(121)
