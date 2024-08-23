# text = '''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."'''
# print(text)

# x = input()
# y = input()
#
# print("Hello", x, y,"! You have just delved into Python",sep=("")

# team = input()
#
# print('Футбольная команда', team, 'имеет длину', len(team), 'символов')

# a, b, c = input(), input(), input()
#
# city1 = len(a)
# city2 = len(b)
# city3 = len(c)
#
# lenmax = max(city1, city2, city3)
# lenmin = min(city1, city2, city3)
#
# if lenmax == city1:
#     maxcity = a
# elif lenmax == city2:
#     maxcity = b
# else:
#     maxcity = c
#
# if lenmin == city1:
#     mincity = a
# elif lenmin == city2:
#     mincity = b
# else:
#     mincity = c
#
# print(mincity, maxcity, sep=('\n'))

# a, b, c = len(input()), len(input()), len(input())
#
# if (2 * b - c - a) * (2 * a - c - b) * (2 * c - a - b) == 0:
#     print('YES')
# else:
#     print("NO")

# text = input()
#
# if "суббота" in text or 'воскресенье' in text:
#     print('YES')
# else:
#     print("NO")

email = input()

if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')