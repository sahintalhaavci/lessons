# comprehasion - это генерация цыклы в одну строку (синтетический сахар это укратить код)

# основноый цель использивание как list , dict , comprehesion является упрощение и повышение читаемести кода 

# list comprehesion - это упращенный подход к создании кода  который задейсвует цыкл for 
# а так же модем использовать if else операторы 

# под капотом генератоп списка такие использовает цыкл for но по скорости он быстрее потому что использовает метод append

# list_ = []

# for i in range(1,11):
#     list_.append(i**2)

# print(list_)


# list_ = [i **2 for i in range(1,11)] #вот так 

# результат for элемент in итерируемый объект 

# import time

# start_time = time.time()
# list1 = []
# for i in range(100):
#     list1.append(i)
#     time1 = time.time() - start_time
# print(time1)



# start_time1 = time.time() #11:42
# list2=[i for i in range(100)] #работа кода 
# time2 = time.time() - start_time1 #11:43 - 11:42 = 1
# print(time2)


# list3 = [i for i in range(1,11) if not i&2]
# print(list3)

# print([input("text :")for i in range(10)])


#еслм в условии нужен else то все условие пишется до for 

# list_ = ['нечетный' if i %2 else 'четный'for i in range(11)]
# print(list_)
# # ---------

# list1 = [1,'hello',2,'a',4.0,'7',8]
# a= ['нечетный 'if i %2 else'четное' for i in range(11) if type(i) == 'int' or type(i) == 'float']
# print(a)



# list_ = [1,2,3,4,5,6,5,6,7,6,3,]
# set_ = {i for i in list_}
# print(set_)

# dict comprehesion - аналогтчно создается , но обязательно нужно указывать key:vaule

# squad = {i:i ** i for i in range(11)}
# print(squad)

# d  = {'a:':2,'b':3}

# list_ = {i:str(i)for i in range(10)}
# print(list_)



# dict_ = {'a':1,'b':,'c':3}

# dict2={vaule:key for vaule,key dict_.items()}




# dict1 = {
#     "a":[1,2,3,4,5],
#     "b":[10,30,2,5],
#     "c":[74,28,47],
#     "d":[4,6,2,92,9]
#     }

# dict2 = {key:sum(value)for key,value in dict1.items() }
# print(dict2)

a = int(input('ввдеите сумму :'))

b = (i for i in a)
print(b)