def select(f, col):
    return [f(x) for  x in col]

def where(f, col):
    return [x for x in col if f(x)]