k = int(input())
m = int(input())
n = int(input())

p = n / k
if k >= 1 and m >= 0 and n >= 1:
    if p < 1:
        t = m * 2
        print(t)
    elif p == int(p):
        t = m * 2 * p
        print(t)
    else:
        x = int(p) + 1
        t = m * 2 * x
        print(t)