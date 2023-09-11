# lambda - анонимная функция


# def add_nums(a,b): return a+b

# print(add_nums(2,3))


# result = lambda a,b: a+b

# print(result(1,3))




# x = lambda x,y,z:(x*y)%z

# print(x(5,7,10))
# x = {'1':2,'2':3}
# get_key = lambda x: x.keys()

# print(get_key(x))

# square = lambda a:a **2

# print(square(3))



# list_ = ['hello ','world']
# get_last = lambda ls : ls[-1]

# print(get_last(list_))


# map(function,iterable) функция который принимает функцию а потои итерируемый объект (можно испрользовть как функция)

#он проходит по каждый элемент!

# map_gen = map(int,['1','2','3','4','5'])
# print(tuple(map_gen))

# def square(number:int):
#     return number*number
# nums = [1,2,3,4,5]
# map_gen = map(square, nums)

# print(tuple(map_gen))


# list_ = [1,-3,0,44,-100]

# list_2 = list(map(lambda x:x<0 , list_))
# print(list_2)

# func = lambda e: e+1
# res = []
# for e in [1,2,3,4,5,6,7]: --------> можно так использовать 
#     res.append(func(e))
# print(res)


# filter(function , iterable) - функция принимает с начало другую функцию потом итерируемый объект
# результатом будет последовательность который прошли условие filter





num1 = [1,2,3,4,5,6,7,8,9,10]
# def filternums(number):
#     if number %2== 0:
#         return True

# result = list(filter(filternums,num1))

# print(result)


# filternums = lambda nums:nums %2 == 0
# print(list(filter(filternums,num1))) # --------> можно так с помощи lambada


# res = list(filter(lambda num: num %2 == 0 , num1))
# print(res)


list_ = ['Nurs', 'John','Bella','Oomat','LoL']

# def stw(name):
#     vowels = 'NJBO'
    # return name.upper().startswith(tuple(vowels))
# print(stw('Nahuy'))

# res = list(filter(stw,list_))
# print(res)




# list_ = ['Nurs', 'John','Bella','Oomat','LoL']

# def stw(name):
#     vowels = 'NJBO'
#     return name.upper().startswith(tuple(vowels))

# res = []                                          -----------------> вот так будет работать без фильтр

# for name in list_:
#     if stw(name):
#         res.append(name)

# print(res)





# reduce  - это функция тоже принимает функцию и вернет 1 результат (его надо импортировать)

from functools import reduce

# list_ [1,2,3,4,5]

# result = reduce(lambda x,y:x+y,list_)
# print(result)





# lst = [*range(1,80000000)]

# def nul(a,b):
#     return a*b

# res = reduce(nul,lst)
# print(res)


# enumerate(iterable , [start - с какого начинать элемента по дефолту 0])

# функция принимает последовательность возращает tuple состящий из числа и элемента

# lst = ['a','b','c','d']

# for i in enumerate(lst):
#     print(i)


lst = ['a','b','c','d']
# for i in enumerate(lst[1:]):
#     print(i)

for i in enumerate(lst,5): #index начинает с 5
    pass


# zip(iterable , iterable .........) сопоставляет каждый элемент из iterable со следующим

# list1 = [*range(1,6)]
# list2 = [*range(10,100)]
# print(list(zip(list1,list2)))






# any(iterable) возращает true если хотя бы один элемент в iterable имеет значение True
# my_list = [False , False]

# all(iterable) возращает true если все элементы является True


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = map(lambda x : if x %2:'lol' else: '1' , lst)

print(res)