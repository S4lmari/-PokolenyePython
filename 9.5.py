from itertools import count
from sys import flags

# n = int(input())
#
# for i in range(1,n+1):
#     c = input()
#     if c.isspace() == True or c == "":
#         print(i,": ","COMMENT SHOULD BE DELETED",sep="")
#     else:
#         print(i,": ",c,sep="")

number = input()
count = 0
checksymbol = "АВЕКМНОРСТУХ"
checknum = "0123456789"
if len(number) >= 9 and number[6] == "_":
    if number[0] in checksymbol:
        count += 1
    for i in number[1:4]:
        if i in checknum:
            count += 1
    for i in number[4:6]:
        if i in checksymbol:
            count += 1
    for i in number[7:]:
        if i in checknum:
            count += 1

if len(number) == 9 and count == 8:
    print("YES", count)
elif len(number) == 10 and count == 9:
    print("YES", count)
else:
    print("NO", count)
