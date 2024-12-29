# s = 'Python rocks!'
# print(s.replace("s","@"))


# st = input()
# new = ""
# for i in range(len(st)):
#     if i % 3 == 0:
#         continue
#     new += st[i]
# print(new)

# st = input()
# print(st.replace("1","one"))

# st = input()
# print(st.replace("@",""))

# st = input()
# count = -2
# list = []
# for i in range(len(st)):
#     if st[i] == "f":
#         count += 1
#         list.append(i)
# if count >=0:
#     print(list[1])
# elif count == -1:
#     print(count)
# else:
#     print(count)

st = input()
first_h = st.find('h')
second_h = st.rfind('h')
new = ""
for i in range(second_h,first_h,-1):
    new += st[i]
print(st[:first_h],new,st[second_h:],sep='')

