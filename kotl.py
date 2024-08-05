k = int(input())
m = int(input())
n = int(input())


if k >= 1 and m >= 0 and n >= 1:
    div, mod = divmod(n, k)
    print((div + 1 - 0 ** mod) * m * 2)
else:
    