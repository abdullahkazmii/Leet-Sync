def patter_1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


def patter_2(n):
    for i in range(1, n):
        for j in range(i):
            print("*", end="")
        print()


def patter_3(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            print(j, end="")
        print()


def patter_4(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            print(i, end="")
        print()


def pattern_5(n):
    for i in range(1, n):
        for j in range(n - i):
            print("*", end="")
        print()


def pattern_6(n):
    for i in range(1, n):
        for j in range(1, n - i + 1):
            print(j, end="")
        print()


def pattern_7(n):
    for i in range(n):
        for _ in range(n - i - 1):
            print(" ", end=" ")

        for _ in range(2 * i + 1):
            print("*", end=" ")

        for _ in range(n - i - 1):
            print(" ", end=" ")

        print()


def pattern_8(n):
    for i in range(n):
        for _ in range(i):
            print(" ", end=" ")

        for _ in range(2 * n - (2 * i + 1)):
            print("*", end=" ")

        for _ in range(i):
            print(" ", end=" ")

        print()


def pattern_9(n):
    for i in range(n):
        for _ in range(n - i - 1):
            print(" ", end=" ")

        for _ in range(2 * i + 1):
            print("*", end=" ")

        for _ in range(n - i - 1):
            print(" ", end=" ")

        print()
    for i in range(n):
        for _ in range(i):
            print(" ", end=" ")

        for _ in range(2 * n - (2 * i + 1)):
            print("*", end=" ")

        for _ in range(i):
            print(" ", end=" ")

        print()


def pattern_10(n):
    for i in range(2 * n - 1):
        stars = i + 1
        if i >= n:
            stars = 2 * n - i - 1
        for _ in range(stars):
            print("*", end=" ")
        print()


def pattern_11(n):
    start = 1
    for i in range(n):
        start = 1 if (i % 2) == 0 else 0
        for _ in range(i + 1):
            print(start, end="")
            start = 1 - start
        print()


def pattern_12(n):
    space = 2 * (n - 1)
    for i in range(1, n + 1):
        # print("=======> n value ", n)
        # numbers
        for j in range(1, i + 1):
            print(j, end="")

        # spaces
        for j in range(space):
            print(" ", end="")
        # numbers
        for j in range(i, 0, -1):
            print(j, end="")
        print()
        space -= 2


def pattern_13(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
