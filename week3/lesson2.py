#Try ,except
# исключение и ошибки - объекты которые перерывает коды

# ошибки - проблема в синтексисе которые мы исправляем самостоятельно

# 1.SyntaxError - забыли двоеточие , не правльно назвали пременную , забыли кавычку
# 2ф= 'name'
# name = 'fls"
# list_ = [1324,324,234
#===========================

# 2.IndentationError - ошибка в табулации

# while True:
# print('1')

# for i in range(10):
# print(i)

#=====================
# TabError - неверная табулация (смешивание пробел и tab )

# while True:
    #  print('h')

#========================

#исключение ; (код написан правильно верно , но программа работает не так как ожидалось)


# ZeroDivisionError - выходит при делении на ноль
# print(40/0)
# print(3//0)
# print(3%0)
#===================
# NameError - исключение выходит когда мы обращаемся к несуществеющей пепременной
# a = 1
# print(b)
#===================
# IndexError - исключение которык выходит когда хотим обратиться несуществуему индексу
list_ = [1,2,3,4]
# print(list_[3]) --> 3
# print(list_[6]) --> ошибка нету такого индекса
#===================
# KeyError - исключение выходить когда мы обращаемся несуществующему ключи
dict_ = {'a':2}
# dict_.pop('b') --> KeyError
# print(dict_['b']) --> KeyError
# ===================
# ImportError - исключение в импротации 
# from math input pi2 -> ImportError 'pi2' not found
# =======================
# ValueError - когла в функции передаем не тот тип данных 
# a,b,c = 1,2,
# print(a,b,c) -ValueError 
#========================
# TypeError - когда мы пытаемся использовть методы не свойственны какому типу данных либо не когда
# мы передаем функции больше или меньше аргументов чем ожидает функция

# for i in 123213: --> ValueError
    # print(i)

# print(5+'5') - ValueError
#==========================

# AttributeError - выходит когда мы обращаемся несуществующему аттирубуту или методу объекту
# [].replace('a' , " ") - AttributeError replace для str
# ''.pop() - AttributeError потому что это функция для list , dict
#==========================
# BaseException() - все ощибки находится тут


# try except
#мы использиваем это страение для того чтобы наш код не перекращал работу

# try:
    #код который может вызвать ошибку
# except:
    #код который сработает если в try вышла ошибка
# else:
    # код который сработает если в try не вышла ошибка
# finally:
    # код который сработает в любом случае 

# try:
#     num1 = int(input(''))
#     num2 = int(input(''))
#     result = num1+num2
#     print(result)
# except ValueError:
#     print('Введите Число')

# try:
#     result = a*2
#     print(result)
# except Exception as e:
#     print(f'')
# list_ = [1,2,3]
# AttributeError
# try:
#     list2 = list_.get()
# except (SyntaxError,AttributeError):
#     pass
[1,2,3,4,5,6,7,8,9,10].clear