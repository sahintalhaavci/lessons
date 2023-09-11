# def decor_func(func): #должен принимать функцию
#     print('decor func')
#     return func()

# def func():
#     print('func2')
#     return 'hello'

# res = decor_func(func)
# print(res)


# декаратор - это функция который принимает другую функцию
# Декоратор является высшего порядка это функция которые могут принять как аргумент другую функцию и вернуть ее 
# Декоратор модификцирвует  и улучшает принутую функцию и выдает изменную 

# def func2(func):
#     print('Я буду работать до функции func1')
#     print(func())

# def func1():
#     return 'Функция deco завершилось'


# func2(func1)

# def to_upper(f):
#     def wrapper():
#         original_res = f()
#         modified_res = original_res.upper()
#     return wrapper

# @to_upper что бы быстрее вызвать декорации
# def some_words():
#     return 'Hello World'

# def some_words1():
#     return 'hello kyrgyzstan'

# print(some_words())



# def get_name(name):
#     return name

# def get_age(age):
#     return age

# def get_last_name(last_name):
#     return last_name

# print(get_name('john'))
# print(get_age(14))
# print(get_last_name('Snow'))


# def decorator_func(func):
#     def wrapper(some_info):
#         return 'Вы Передали: ' + str(func(some_info))
#     return wrapper

# @decorator_func
# def get_name(name):
#     return name

# @decorator_func
# def get_age(age):
#     return age

# @decorator_func
# def get_last_name(last_name):
#     return last_name

# print(get_name('Name'))


# def func_def(fuction_to_decorate): #сюда попадает функция которую нужно задекрировать 
#     def wrapper(): #обертояная оболочка для функции
#         print('Я код , который отробатывает до вызова функции')
#         fuction_to_decorate()


# если мы используем аргументы у функции то мы обеязательно должны передавать их в декартор

# def decorator(func):
#     def wrapper(arg):
#         print(f'Смотри что я принимаю {arg}')
#         func(arg)
#     return wrapper
# @decorator
# def func1(word):
#     print(f'Я принимаю в себя слово {word}')

# func1('yes')









# def decorator(func): #лучше использвать такой запись потому-что оно является универсальный для всех
#     def wrapper(*args,**kwargs):
#         print(f'здесь args {args}')
#         print(f'здесь кваргс {kwargs}')
#         func(*args , **kwargs)
#     return wrapper
# @decorator
# def func_without_parameters():
#     print('функция без параметров')
# @decorator
# def func_with_parametrs(first_name , last_name):
#     print('функция с параметрами ')
#     print(f'hello {first_name}, {last_name}')
# @decorator
# def func_with_parametrs_kwargs(first_name, last_name):
#     print('функция с параметрами ')
#     print(f'hello {first_name}, {last_name}')

# func_without_parameters()
# func_with_parametrs('John','Snow')
# func_with_parametrs_kwargs(first_name='John',last_name='Snow')



# def div(func):
#     print('f')
#     def wrapper(*args,**kwargs):
#         print(func.__name__)
#         return "<div>"+func(*args , **kwargs)+ "</div"
#     return

# @div
# def get(name,lastname):
#     print('f2')
#     return name + lastname

# print(get('John' ,'Snow'))



# def bread(func):
#     def wrapper(*args , **kwargs):
#         return 'bread' + str(func(*args , **kwargs)) + 'bread'
#     return wrapper
# def ingredients(func):
#     def wrapper(*args , **kwargs):
#         return 'tomato' + str(func(*args , **kwargs)) + 'salad'
#     return wrapper
# @bread
# @ingredients
# def get_sandwich(x):
#     print(x)
#     return x
# print(get_sandwich('sas'))



# def my_decorator(func):
#     print('Am i Decorate?')
#     def wrapper():
#         print('am i wrapper? cmon')
#         return func
#     print("It's Last Print Bro :D ")
#     return wrapper
# @my_decorator
# def decorate_function():
#     print('Am i Second? ')
# decorate_function()

import requests
def benchmark(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Function Worked :{end-start}')
    return wrapper
@benchmark
def call_webpage():
    webpage = requests.get('https://google.com')

call_webpage()