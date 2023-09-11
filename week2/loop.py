#Цыклы - это блок кода ,  который повтрояется опердиленная количество раз и есть повторяется бескончно

# for - цыкл - который работает с итеруремый обьектами и законить свою работу на последнем элементе 

# while - цыкл который работет пока условие верно

# while True: # пока правда 
#     print('Hello')
#     #после while идет условие цыкла пока это условие правда , то цыкл будет работать


# counter = 0

# while True:
#     counter +=1
#     print(counter   )



# count = 10

# while count != 0:
#     print(count)
#     count = count-1


# a = 0
# while a:
#     print('hello') #не будет работать потому-что 0 = false


# for i in range(10):
#     print(i)

# num = 12345678
# sum = 0
# for i in str(num):
#     sum += int(i)

# print(sum)





# string = "hello"
# string1 = "world"
# for i in range(len(string)):
#     print(i , string[i],string1[i])


# list_ = [1,2,3]
# for i in list_:
#     print(i)
#     list_.append('hello')


#ключевые слова

# break - польностю выйти из цыкла дострочно прерывает цыкл
# continue - перейти следущий итератции

# for i in range(10):
#     if i ==3:
#         continue
#     print(i)


# for i in range(10):
#     print(i)
#     if i ==3:
#         continue

# for i in range(10):
#     print(i)
#     if i ==3:
#         break


i = 0

while i <6:
    i+=1
    if i ==3:
        break
    else:
        print(i)
        i+= 1


#else примененные цыкле for while проверяет был ли призведен цыкла break или же естестивенным оброзом
# else работает если выход получен без break 

for i in 'hello world':
    if i == 'd':
        break
else:
    print('hello world')

for num in range(5):
    if num<3:
        pass
    else:
        print(num)


dict1 = ['a':1,'b':2,'c':3]

for key in dict1:
    print(key) #что бы получпть key данного словарь


for keys in dict1:
    print(keys[key]) #что бы получать данные в внутри key 



my_dict = {'a':1,'b':2,'c':3}
keys = []
for key in my_dict:
    keys.append(key)
pass1 = input("пароль")
