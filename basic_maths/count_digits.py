def extract(n):
    sum = 0
    while n > 0:
        last = n % 10
        sum = sum + 1
        print(last)
        n = n // 10
    print("Sum:", sum)


extract(5579)
