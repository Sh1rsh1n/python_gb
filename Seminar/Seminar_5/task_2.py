from random import choices


def fill_list(num):
    return choices(range(num * 2), k=num)


ls = fill_list(10)
print(ls)

def find_sublist(list):
    ls = []
    for i in range(len(list)):
        curr = list[i]
        curr_ls = [curr]
        for j in range(i, len(list)):
            if (list[j] > curr):
                curr_ls.append(list[j])
                curr = list[j]
        if len(curr_ls) > 1:
            ls.append(curr_ls)
    return ls


print(find_sublist(ls))
