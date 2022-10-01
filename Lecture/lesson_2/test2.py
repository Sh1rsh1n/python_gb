def concat(*params):
    res: str = ''
    for item in params:
        res += item + " "
    return res


print(concat('my', 'name', 'is', 'alex'))