#  Пронстрантво имен

# 1. __builtins__ - (встроенные имен) - все что встроено в python 

# print(dir(__builtins__)) - что бы посмотреть функции

# 2.. global - все переменные внутри файла которые мы создали

# enclosed - пространство находящийся между двумя пространстве ( между global и local)

# local - локальная пространство имен
# по меры выполнение програмы python  создает разные пространство имен и удаляет их

# a = 10
# b = 'hello'
# print(globals)

# x = 10
# print(globals()['x'])

# globals - возращает словарь с глобальным переменныс

# def hello():
#     a = 'hello world'
#     print(locals())
# hello()

# def func(b,c):
#     a= 5
#     print(locals)


# enclosed - она возникает тогда , когда есть вложенности в функции 
# x = 'глобальная област видомости'
# def same_func():
#     x = 'это enclosed область видимости '
#     print(x)
#     def same_func2():
#         x = 'это локальная область видимости'


# def func():
#     a = 'func'
#     # enclosed пространство 
#     def inner_func():
#         #локальная пространство 
#         a = 'int'
#         print(locals)


# def func():

#     aa = input('lol')

# print(aa)


count = 0

# def counter():
#     try:
#         print(count)
#         count+=1
#     except:
#         print('f')
# print(type(count))
# def counter():
#     global count
#     count += 1
#     print(count)

# def outer_fuction():
#     a = 20
#     def inner_function():
#         global a
#         a = 30
#         print(f'inner function a = {a}')
#     inner_function()
#     print(f'outer fuction a= {a}')

# a= 10
# outer_fuction()


# def func():
#     a = '1'
#     def inner_func():
#         def inner_func2():
#             nonlocal a
#             a = 2
#         inner_func2()
#     inner_func()
#     print(a)
# func()


# def enclosed():
#     x = 20
#     def local():
#         nonlocal x
#         x = 'Edited enclosed X'
#         print(f'{x} is local')
#     local()
#     print(f'{x} is enclosed')
# enclosed()



# def func():
#     var = 100
#     def nested():
#         nonlocal var
#         var += 100
#     nested()
#     print(var)
# func()





# def count(i:int):
#     counter = 0

#     def add():
#         nonlocal counter
#         print(counter)
#         counter+=1

#     for x in range(i):
#         add()

# count(10)


def enclosed():
    x = 20
    def local():
        nonlocal x
        x = 30
    print(f'{x} enclosed')

    local()
