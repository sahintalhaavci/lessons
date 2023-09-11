

# users = {'0':'User1','1':'User2','2':'User3'}
# user = {value:key for value,key in users.items()}
# name = input('Введите Ник :')


Exception
# dict1 = {1: 'user1', 2: 'user2', 3: 'user3'}
# dict1 = {value: key for key, value in dict1.items()}
# print(dict1)
# try:
#     username = input('enter username: ')
#     id1 = dict1[username]
#     print(id1)
# except KeyError:
#     print('Введенного username нет в базе данных')
# else:
#     print(f'Добро пожаловать {username}')
# finally:
#     print('спасибо')



# try: 
#     age = int(input()) 
#     if age < 18: 
#         raise ValueError('Доступ запрещён') 
# except ValueError: 
#     print('Введён некорректный возраст') 
# else: 
#     print('Спасибо') 
# finally: 
#     print('До свидания!')


# [1,2,3,4,5,6,7,8,9,10]
# try:
#     a = []
#     [0,1,2,3,4,5,6,7,8,9,10].index()
# except SyntaxError:
#     print(' ')





# a = int(input('Введите Цифру :'))
# b = int(input('Введите Цифру :'))
# def number(a:int,b:int)->int:
#     print(a+b)


# def my_len(obj):
#     count = 0
#     for i in obj:
#         count +=1
#     print(count)

# my_len('lol')


# def checker(x,y):
#     for i in x,y:
#         print(type(i))

# checker(['test'],'lol')
# x = int(input('Введите Цифру :'))
# y = int(input('Введите Цифру :'))
# def cal(x:int,y:int)->int:
#     print(x/y)

# cal(x,y)


# dict_ = {'a':1,'b':2,'c':3,'lollol':4}
# dict2 = {}
# def keys(words):
#         dict2=dict_.keys()
#         print(dict2)
# keys(dict_)

# def odd_or(number:int)->str:
#     if number %2 == 1:
#         print("It's Odder")
#     elif number %2 >= 0:
#         print("It's Even Number")
#     else:
#         print('Error')
# try:

#     number = int(input('Введите Цифру'))
#     odd_or(number)
# except ValueError:
#     print("Please Type INT!")



# def cal(x:int,y:int)->int:
#     print(int(x/y))
# try:
#   x = int(input('Введите Цифру :'))
#   y = int(input('Введите Цифру :'))
#   cal(x,y)
# except (ZeroDivisionError,ValueError):
#   print('Type INT Or Not Type 0!')




# list_ = ['olo','lol','hello','world','aziza']

# def palidrom(words:list)->list:
#     palidrom1 =[]
#     for word in words:
#         if word in words[::-1]:
#             palidrom1.append(word)
#         else:
#             continue
#     return palidrom1
# print(palidrom(list_)) 

# def func(x,y):
#     if x>y:
#         print(x)
#     elif y>x:
#         print(y)
#     else:
#         print('Error')
# try:
#     x = int(input('Введите Число :'))
#     y = int(input('Введите Число :'))
#     func(x,y)
# except ValueError:
#     print('Type INT')   




# password = input('Введите Пароль')

# try:
#     if password <6:
#         raise Exception('ValueError')
# except Exception:
#     print('Error')



a = {'a':1,'b':2}

print(a.pop(1))
