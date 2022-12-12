# def select(f,col):
#     return[f(x) for x in col]

# def where (f,col):
#     return[x for x in col if f(x)]

# data ='1 2 3 4 5 8 15 23 38'.split()

# res = select(int,data)
# res = where(lambda x: not x%2,res)
# res = select(lambda x: (x,x**2),res)
# print(res)


# li = [x for x in range(1,20)]

# li = list( map(lambda x:x+10,li))

# print(li)

# data = list(map(int,input().split()))
# print(data)

# data = [x for x in range(10)]

# res = list(filter(lambda x: x%2==0, data))
# print(res)

# def func(x):
# return x ** 2
#
# res = func(3)
# print(res)

# res = lambda x: x ** 2
# print(res(3))

# def ispositive(x):
# return x > 0

# sp = [1, -5, 3, -7, 8]
# # res = list(filter(ispositive, sp))
# res = list(filter(lambda s: s > 0, sp))
# # print(res)


# def kvadrat(x):
# return x ** 2

# sp = [1, 2, 3, 4, 5]
# # res = list(map(kvadrat, sp))
# res = list(map(lambda a: a ** 2, sp))
# # print(res)

# # Сортировка
# sp = ['rrr', 'z', 'tyjuuu', 'aaaaaaaaaaa']
# sp.sort(key=lambda a: -len(a))
# sp.sort(key=lambda a: len(a), reverse=True)
# # print(sp)

# sp = [['a', 66], ['b', 66], ['c', 1], ['d', 1]]
# sp.sort(key=lambda x: (-x[1], x[0]))
# # print(sp)

# # Списочные выражения
# sp = [i * 10 for i in range(1, 100) if i % 4 == 0]
# # print(sp)

# a, b, c = [int(i) for i in input("Введите значения A,B,C: ").split()]
# print(a + b + c)

