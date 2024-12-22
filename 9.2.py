# s = input()
#
# if s == s[::-1]:
#     print('YES')
# else:
#     print("NO")

# s = input()
#
# print(len(s),s*3,s[0],s[:3],s[-3:],s[::-1],s[1:len(s)],sep="\n")

s = input()

print(s[2],s[-2],s[:5],s[:len(s)-2],s[::2],s[1::2],s[::-1],s[::-2],sep='\n')