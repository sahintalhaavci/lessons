import random

# Логические врожение и операторы :


# Boolen

# print('') - false
# print(' ') - True 


# == - равно

# print(5 == 5) - True
# print(5 == 2) - False

# != - не равно

# print(5 != 2) - True
# print(5 != 5) - False

# >< - меньше или больще

# print(1>2) - True
# print(2>1) - False

#Логические Операции

# a. and
# b. or
# c. not

# a = 5
# b = 6

# print(a == 5 and b == 6) - True
# print(a == 6 and b == 5) - False
# ----------------------------------- #
# print(a ==6 or b == 5) - True
# print(a ==5 or b == 7) - False
# ----------------------------------- #
# print(not False) - True
# print(not True ) - False


# Cравнение 

# a. == - равно 
# b . is = сравнение по ячейкам 
# a = 5
# a= 6
# print(a ==b) - True



# Условные Операторы

# Условные операторы должны для того чтобы при разных введенных данных код работал по разному 

# if условие1:
    # код

# if условие1:
    # код

# else:
    # код
        # если if не выполниться
        
# ---------------------------------- #

# if условие1:
    # код

# elif условие2:
    # код
        #ecли if не выполниться
# else:
    # код
        # если if или elif не выполниться

# в одной конструкции может быть только 1 if!!

# мы можем использивать бесконечно полсле if (он не работает без if)!

# мы можем использивать 1 раз использивать elif конца конструкции (без if не работает)


# a = 'Hello'

# if 'h' in a:
#     print('Worked')
# if a :
#     print('Worked')
# if len(a)>3:


# age = int(input("ваш возраст :"))

# if age >= 18:
#     print("можете войти")
# else:
#     print('Вам нельзя войти')



# number = int(input(""))


# if  (number%2)== 0:
#     print("Success")

# else:
#     print("False")






# Тернаные Операторы 

# телo1 if  условие else тело2

# a = 5
# res = 'Hello' ifa ==4 else 'Bye' #если а равно 5 в res будет храниться hello если не так напшет Bye


# Морковый оператор позвялет нам как присваивать значение переменной ,таки возращает ее значение

# print(num:= 15) это функция добавляет переменный в num (работает только в print!)


# operator = input('Введите Оператор Число (+ , -  , * , /)')

# number1 = int(input("Введите Первое Число: "))
# number2 = int(input("Введите Второе Число: ")

# if operator == '+':
#     print(number1 +number2)
# elif operator == '-':
#     print('number1 - number2')
# elif operator == '*':
#     print(number1 *number2)




# # ---- FizzBuzz ---- #

# number = int(input("Число"))
# try:
#     number = int()
# if number%3 == 0 and number%5 == 0:
#     print("FIZZBUZZ")
# elif(number%3) == 0:
#     print("BUZZ")
# elif(number%5) == 0:
#     print("BUZZ")
# else:
#     print(number)


# name = input('Имя')
# fr = int(input('Количество Друзей:'))

# a = f"У {name} , {fr} Друзей" if fr >= 2 else f"У {name} ,{fr} Друг "

# print(a)


# x = int(input('Первое Число :'))
# y = int(input('Второе Число :'))
# z = int(input('Третие Число :'))

# if x == y and x == z:
#     print("равностронный")

# elif x == y or x == z or y ==x or 






# pas = input("Пароль :")
# symbol = '! , @ , #, $'
# if pass.len(8) and pass.isalnum() and pass in symbol: 
#     print('Sucess')