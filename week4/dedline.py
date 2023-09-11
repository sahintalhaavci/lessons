import datetime

data = [
    {
        "id": 1,
        "name": "iphone 15 pro max",
        "price": 90000,
        "created_a": datetime.datetime(2024, 12, 20),
        "is_active": True
    },
    {
        "id": 2,
        "name": "Samsuka galactica not 10",
        "price": 60000,
        "created_a": datetime.datetime(2021, 6, 15),
        "is_active": True
    },
    {
        "id": 3,
        "name": "Play_station",
        "price": 45000,
        "created_a": datetime.datetime(2022, 7, 30),
        "is_active": False
    }
]


def get_all():
    return data

def get_one(id):
    product = [i for i in data if i["id"] == id]
    if product:
        return product
    return "Нет такого продукта"


def post_product():
    max_id = max([i['id'] for i in data])
    new_data = {
        "id": max_id + 1,
        "name": input("Name: ").title(),
        "price": int(input("Price: ")),
        "crated_at": datetime.datetime.now(),
        "is_active": True
    }

    data.append(new_data)
    return '201 CRATED', new_data

def patch_product(id):
    product = [i for i in data if i['id'] == id]
    index = data.index(product[0])
    if product:
        data.remove(product[0])
        name = input("Name: ").title()
        price = int(input("Price: "))
        product[0]['name'] = name
        product[0]['price'] = price
        product[0]['created_a'] = datetime.datetime.now()
        product[0]['is_active'] = True
        data.insert(index, product[0])
        return 'Успешно изменен'
    else:
        return 'Вы ввели неправильные данные'    


def del_product(id):
    product = [i for i in data if i['id'] == id]
    if product:
        index = data.index(product[0])
        data.pop(index)
        return 'Удален'
    else:
        print('Такого продукта нет')


def main():
    print("Дарова, тебе доступны следущие функции:\n\tGET\n\tPOST\n\tDETAIL\n\tPUT\n\tDELETE")
    method = input("Выберите одну из функций: ").lower()
    if method == 'get':
        print(get_all())

    elif method == 'detail':
        id = int(input("Введите ID: "))
        print(get_one(id))

    elif method == 'post':
        print(post_product())

    elif method == 'put':
        id = int(input("Введите ID: "))
        print(patch_product(id))
    
    elif method == 'delete':
        id = int(input("Введите ID: "))
        print(del_product(id))

main()