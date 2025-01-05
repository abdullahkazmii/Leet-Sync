def patter_1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("| i = ", i, "| j = ", j)


def patter_2(n):
    for i in range(1, n):
        for j in range(i):
            print("*", end="")
        print(i)


def patter_3(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            print(j, end="")
        print("| i = ", i, "| j = ", j)


def patter_4(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            print(i, end="")
        print("| i = ", i, "| j = ", j)


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


pattern_10(5)


def pattern_11(n):
    start = 1
    for i in range(n):
        start = 1 if (i % 2) == 0 else 0
        for _ in range(i + 1):
            print(start, end="")
            start = 1 - start
        print()


pattern_11(5)
