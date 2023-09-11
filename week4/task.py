# def get_type(par,par1):
#     print(type(par))
#     print(type(par1))
#     return
# get_type('a',1)


# def text():
#     tex = input('Введите Текст Для Добавление (Максимиум 60 Символов!): ').capitalize()
#     if len(tex) < 60 :
#         print('1')
#     elif len(tex) >= 60 :
#         print('Максимум 60 Символов!!')
#     else:
#         print('Системная Ошибка :/ ')

# text()



x = [1,'2',3,'4']
# res  = map(int , x)
# res(x)

# map_gen = map(int,x)
# print(tuple(map_gen))
# y = lambda x : x**float(0.5)
# print(y(map_gen))

num1 = [1,2,3,4,5,6,7,8,9,10]
filternums = lambda nums:nums **0.5
print(list(filter(filternums,x)))








# from functools import reduce
# list_ = ['h','e','l','l','o','w','o','r','l','d']
# result = reduce(lambda x, y: x + y, list_)
# print(result)