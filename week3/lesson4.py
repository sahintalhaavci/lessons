#Функции это именованный блок кода ,который выполянет одну задачу и может себя принимать аргументы и возращать какое-то значение
#Функцию можно вызывать по индексу,обращасть по индексу
# def - ключевое слово , указывает python что мы хртим создать функцию называние функции это переменная прд этим именме python запоминает называние функции
# скобки нужнр для того чтр бы функция могла принимать параметры

# Синтаксис
# def называние_функции(аргументы):
    # принимаем аргументы для работы в теле называние_функции

def my_sum(x,y):
    print(x+y)
    return x+y #что бы сохранять нужно

def my_len(obj):
    count = 0
    for i in obj:
        count +=1
    print(count)


res = my_sum(5,6)
print(res)

# return - использувется для возращаение результата и на этом моменте функция заверщает свою работу
# return - это ключевое слова , которые дает понять python  что за этой командой будет какая то информации  которая является окончательным результатом нашей функции




#Распоковка

# list1 = list(range[1,11])
# print(list1)

# list1 = [*range[1,11]]
# print(list1)



dict1 = {'a':1,'b':2,'c':3}
dict2 = {**dict1}






#не обязательные аргументы args kwars
#args - принимает позицицонные аргументы
# kwards - принимает именновынные аргументы

# args - tuple
# kwards - dict
def two_sum(a,b,*args,**kwards):
    return a+b+sum(args)+sum(kwards.values())

two_sum(1,2,3,4,5,6,7,8,9,0,)


#Анотация

# делает код более имформативным


num: int = 10
str_: str='hello'

def func(a,b:str,c:str) -> int:
    print(a+b+c)



list_ = ['olo','lol','hello','world','aziza']

def palidrom(words:list)->list:
    palidrom1 =[]
    for word in words:
        if word in words[::-1]:
            palidrom1.append(word)
        else:
            continue
    return palidrom1
print(palidrom(list_))



a = {'a':1,'b':2,'c':None,'d':5}

def delete(obj:dict)->dict:
    for key,val in dic.items():
        if val==None:
            dic.pop(key)
    return obj
print(a)

# def validate_email(email:str)->bool:
#     index = email.find('@')
#     if '@'not in email:
#         raise Exception('Invalid email')
#     elif not email


def register(email:str)