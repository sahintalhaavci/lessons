# Cловари  - одно из наболее часто используемый структур данных , позволящий хранить обьекты

# словарь - изменямый итерируемый неидексируемый упрядочный тип данных
#в котором элементы хранится в виде пары ключ значение 

{} - #Литералы 
dict = {} #так можно создать пустую 

dict_ = {'a':'hello' , 'b':1 ,'c':3} # должен быть ключи по им будем ввести данные

dict2 = dict(['keyy1','vaule1'],['key2:', 'vaule2']) #вот так можно создать словарь

dict3 = dict('ab' , 'cd' , 'de') #выдаст a :b , c:d , d:e

dict4 = dict()

dict4['key1'] = 'vaule1' #добавляет key и значение

dct = {'age': 1 , 'age':2} #он будет перезаписивать (не может имееть 2 одинаковых значение)


#=============Методы ;======================

# 1.clear

#Очищает словарь
dct = {'age': 1 , 'age':2}

dct.clear()


#import copy

# 2.Copy

#Копиравние словарья

dct = {'age': 1 , 'age1':2 , 'name': 'jhony'}
dct2 = dct.copy()
print(dct2)


#fromkeys

#создает словарь с ключами из object  и значенем vaule для всех ключей 
#если не передать vaule то у всех ключей будет None

dct = {'age': 1 , 'age':2} 
dct.fromkeys('age' , 'hi') #вот так выглядит параметры нужно указать key потом что мы хотим добавить 


#====Методы получение элементов словаря====


#1.get

# get(key , default) - возращает значение по этому ключу

dct = {'age': 1 , 'age':2}

print(dict.get('ag' , "нету")) #если нет такого ключа то выдаст что мы писали после key тут выдаст нету


# 2.update 

#добавляет новый словапь в над словарь (разширает словапь)


dct = {'age': 1 , 'age':2}
dct1 = {'age2': 1 , 'age2':2}

dct.update(dct1) # Параметры


# 3.setdefault
#это фукция работает как get тоесть проверка key но если не будет данный ключ он создаст новый ключ и будет содержать None



dct = {'age': 1 , 'age':2}

print(dict.setdefault('hey')) #Он выдаст None и создаст новый ключ











# ==== Удаление Элемента =====

# 1. pop
# Удаление key  ( можно его вернуть )если такого key нету то выдаст ошибку мы можем указать ощибку


dct = {'age': 1 , 'age':2}

dct.pop('age' , ['Ошибка'])  #Параметр


# 2.popitem ()

#удаялет и возращает пару ключ значение 

