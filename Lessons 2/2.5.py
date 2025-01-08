# b1 = int(input())
# q = int(input())
# n = int(input())

# bn = b1 * q ** (n - 1)
# print(bn)

# sm = int(input())
# m = sm // 100
# print(m)

# n = int(input())
# k = int(input())
# print(k // n)
# print(k % n)

# n = int(input())
# print(n // 2 + n%2)

# m = int(input())
# h = m // 60
# min = m % 60
# print(m, 'минут - это', h, 'час', min, 'минут')

# n = int(input())
# kype = (n+3) // 4
# print(kype)


# chislo = int(input())
# a = chislo % 10
# b = (chislo % 100) // 10
# c = chislo // 100
# print("Сумма цифр =", a + b + c)
# print("Произведение цифр =", a * b * c)

# chislo = int(input())
# c = chislo % 10
# b = (chislo % 100) // 10
# a = chislo // 100

# print(str(a)+str(b)+str(c),str(a)+str(c)+str(b),str(b)+str(a)+str(c),str(b)+str(c)+str(a),str(c)+str(a)+str(b),str(c)+str(b)+str(a),sep=('\n'))

n = int(input())
t = n//1000
s = (n%1000)//100
d = (n%100)//10
e = n%10
print("Цифра в позиции тысяч равна", t)
print("Цифра в позиции сотен равна", s)
print("Цифра в позиции десятков равна", d)
print("Цифра в позиции единиц равна", e)