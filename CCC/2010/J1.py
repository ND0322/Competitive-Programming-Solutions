n = int(input())

if n < 6:
    if n % 2 == 0:
        print(1 + int(n /2))
    else:
        print(1 + int((n-1) /2))
else:
    if n == 6:
        print(3)
    if n == 7:
        print(2)
    if n == 8:
        print(2)
    if n == 9:
        print(1)
    if n == 10:
        print(10)
