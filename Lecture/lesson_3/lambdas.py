

# def f(x):
#     return x ** 2
#
# g = f
#
#
# print(type(f))
# print(type(g))
#
# print(f(4))
# print(g(4))

# def calc(x):
#     return x + 10
#
# def calc2(x):
#     return x * 10
#
# def math(op, x):
#     print(op(x))
#
# math(calc2, 10)
# math(calc, 10)

# def sum(x, y):
#     return x + y

f = lambda x, y: x + y

# def mult(x, y):
#     return x * y

m = lambda x, y: x * y

def calc(op, a, b):
    print(op(a, b))

calc(f, 4, 5)
calc(m, 4, 5)