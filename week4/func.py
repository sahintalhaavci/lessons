# Crud - 
# create 
# read
# update
# delete
import datetime
data = [
    {
        'id':0,
        'name':'iphone 14',
        'price':80000,
        'created_at': datetime.datetime(2022,9,4),
        'is_active':True
    },
        {
        'id':1,
        'name':'Nokia 3310',
        'price':10000000,
        'created_at': datetime.datetime(1998,1,1),
        'is_active':True
    },
        {
        'id':2,
        'name':'iphone XR',
        'price':32000,
        'created_at': datetime.datetime(2021,9,6),
        'is_active':False
    }
]

def get_all():
    return data


def get_one(id):
    product = [i for i in data if data['id']==id]
    if product:
        return product
    return 'Нет Такого Продукта'        

def post_product():
    max_id = [i['id']for i in data]
    new_data = {
        'id':max_id+1,
        'name':input('Name : '),
        'price':int(input('Price : ')),
        'created_at': datetime.datetime.now(),
        'is_active':True
    }
# data.append(new_data)


def patch_product(id):
    product = [i for i in data if['id']==id]
    if product:
        data.remove(product(0))
        name = input('Name :')
        price = int(input('Price :'))
        is_active = True

patch_product(5)

def delete_product(id):
    del_product = [i for i in data if['id']==id]
    del_product.pop(id)
    return
    
delete_product(1)