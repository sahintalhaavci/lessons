# my_list = [
# {'papato': 3},
# {'milk': 1},
# {'watermaelon': 4},
# {'apple': 2}
# ]
# print(str(my_list))
# while my_list:
#     product_remove  = input('Введите продукт, который вы купили: ')
#     for products in my_list:
#         if product_remove in products:
#             del products[product_remove]
#             print(my_list)

#     if not any(my_list):
#         break
# print('пора на кассу')


# {'papato': 3},{'milk': 1},{'watermaelon': 4},{'apple': 2}


# my_list = [{'papato': 3},{'milk': 1},{'watermaelon': 4},{'apple': 2}]
# print(str(my_list))
# while my_list:
#     product_remove  = input('Введите продукт, который вы купили: ')
#     for products in my_list:
#         if product_remove in products:
#             del products[product_remove]
#             print(my_list)

#     if not any(my_list):
#         break
# print('пора на кассу')


# number = int(input("Cколько Вещей :"))
# for i in range(number):



# quest = input("Номер Человека : ")

# if "первый" in quest:
#      print("Первый")
# elif "второй" in quest:
#      print("второй")
# else:
#      print("Error")


# n = int(input("Enter number below 100: ")) 
# print('На лугу пасется ',end='' ) 
# if (n>100): print("Incorrect number") 
# elif((n>10 and n<20) or (n%10 >= 5) or (n%10==0)): 
#      print(n,"коров") 
# elif(n%10==1 ): 
#      print(n,"корова") 
# elif(n%10 in range(2,5)): 
#      print(n,"коровы")



a = {4, 6, 100, -45, -6}
b = {4, 5, -5, -6}
c = a|b