# Set :

# множество
# Изменяймый тип данных, неупрядоченный , итеруеруемый данные тип данных , неиндексиуемый тип данных, хранит только уникальные значение , хранит только неизменяймый тип данных

set1 = set()

# add(element)
# update(sequrence)

my_set = {1,2,3}
my_set.add(3)
my_set.add('Hello')
my_set.add({1,2,3}) #Error потому-что нельзя добавить изменяймый тип данных


#update

my_set.update([1,2,3,4,5,6,7,8,9])



#Удаление Элемента

#clear

my_set.clear()


#remove() удаляет элемент ,если такого элемента нету то выдаст ошибку
my_set.remove(2)


#dicard удаляет элемент , но если элемента нет , то ничего не происоходит

my_set.discard(2)


# pop() удаляает случайный элемент и может возращать этот элемент

set2 = {1,2,3}

popped = set2.pop()
print(popped)


# difference  выводит эдементы которые одинакивые 

set1 = {1,2,3}
set2 = {2,3,4,5}
print(set1.difference(set2)) #------> {1,2}
print(set1 - set2) #--------> {1,2} либо так можно так же 

#symmetric_difference  вводит элементы которые уникальнык в обоих множествах

a = {1,2,3,4,5}
b = {4,5,6,7}
print(a^b) #------> {1,2,3,6,7} ввыод уникальных элементов
print(a.symmetric_difference(b)) #--------> {1,2,3,6,7}

#intersection вводит одинаквые элементы из set1 и set2

set1 = {1,2,3}
set2 = {2,3,4}

print(set1&set2) #----> {2,3}
print(a.intersection(b)) #------> {2,3}

#union соединает множество 

set1 = {1,2}
set2 = {3,4}

print(set1|set2) #он не сохранает это (что бы сохранить нужно ставить его в переменный)
set3 = print(set1|set2) #вот так 

print(set1.union(set2)) #так же нужно ставить в переменную 

#так же list можно добавить list

list1 = [1,2,3,4,5]
set4 = set1.union(list1) #вот так 

