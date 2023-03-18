def dBinary(num):
    if num > 1:
        dBinary(num // 2)
    print(num % 2, end='')


