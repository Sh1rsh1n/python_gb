# list = []
#
# for i in range(1, 101):
#     if (i % 2 == 0):
#         list.append(i)
# def f(x):
#     return x ** 3
#
#
# list = [f(i) for i in range(1, 21) if i % 2 == 0]
# print(list)


path = 'nums'
f = open(path, 'r')
data = f.read() + ' '
f.close()

num = []
while data != '':
    space = data.index(' ')
    num.append(int(data[:space]))
    data = data[space + 1:]

out = []

for i in num:
    if not i % 2:
        out.append((i, i ** 2))

print(out)