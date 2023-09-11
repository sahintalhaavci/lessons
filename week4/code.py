cate = [
    # {'id':1,
    #  'category':'Web',
    #  'language':'JavaScript',
    #  'difficult':'Normal',
    #  'price':5000
    # },
    # {'id':2,
    #  'category':'Web , Gaming',
    #  'language':'Python',
    #  'difficult':'Easy',
    #  'price':4500
    # },
    # {'id':3,
    #  'category':'Web,Mobile Gaming,Gaming',
    #  'language':'Java',
    #  'difficult':'Hard',
    #  'price':8999,
    # }
]

# def get_info():
#     return cate

# def check_one(id:list)->list:
#     check = [i for i in cate if i['id']== id]
#     if check:
#         return check
#     return 'Ид Не Найден'
cate = [
    {}
]
id = 0
def add_product():
    q = input("Выберите Курс Который Вы Хотите (Web\nGame For Phone\nGaming): ").lower()
    if q in 'web game game for phone' :
        cate.append({'id':id+1})

        add1()
        print(cate)
    else:
        print(f'Нельзя Добавлять {q} Данный!')

def add1():
    q1 = input('Выберите Язык(Python , Java,Javascript) : ').lower()
    if q1 in 'python java javascript':
        text()
    else:
        print(f'Нельзя Добавить {q1} Данный!')

def text():
    tex = input('Введите Текст Для Добавление (Максимиум 60 Символов!): ').capitalize()
    if len(tex) < 60 :
        htext()
    elif len(tex) >=60 :
        print('Максимум 60 Символов!!')
    else:
        print('Системная Ошибка :/ ')

def htext():
    tex2 = input('Введите Текст (10 Слов) :').capitalize()
    if len(tex2) >= 10:
        levels()
    elif len(tex2) < 10:
        print('Текст Должен Быть Не Менее 10 Слов !')
    else:
        print('Системная Ошибка')

def levels():
    level = input('Выберите Сложность (Easy , Normal,Hard):').lower()
    if level in 'easy normal hard':
        price()
    else:
        print(f'Нельзя Добавить {level}')

def price():
    global price1
    global price_i
    try:
        price_i = input('Введите Курс (USD,EUR,KGS) : ').lower()
        price1 = int(input('Укажитие Сумму : '))
        if price_i in 'usd eur kgs':
            convert()
        else:
            print(f'{price_i} Не Принимается!!')
    except ValueError:
        print('Введите INT!')
        price()

def convert():
    usd = 88
    euro = 95
    som = 0
    if price_i == 'usd':
        sum = price1 * usd
        print(sum)
    elif price_i == 'eur':
        sum2 = price1*euro
        print(sum2)
    elif price_i == 'kgs':
        sum3 = price1

add_product()