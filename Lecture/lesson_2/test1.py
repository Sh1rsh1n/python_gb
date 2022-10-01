# colors = ['red', 'green', 'blue']
# data = open("file.txt", "a")
# # data.writelines(colors)
# data.write('LINE 12\n')
# data.write('LINE 13\n')
# data.close()

#
# with open('file.txt', 'w') as data:
#     for i in range(0, 10):
#         data.write(f'line {i + 1} \n')


path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()