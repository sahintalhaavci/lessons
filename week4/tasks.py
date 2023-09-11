while True:
    try:
        equal = input('Please Type Equal(+,-,*,/)')
        number = int(input('Please Type Number :'))
        number2 = int(input('Please Type Second Number :'))
    except (ZeroDivisionError,ValueError):
        print("Please Type Int or Result Don't Be Zero!")
        continue

    def calc(number:int,number2:int)->int:
        if equal == '+':
            print(number+number2)
            return
        elif equal == '-':
            print(number-number2)
            return
        elif equal == '*':
            print(number*number2)
            return
        elif equal == '/':
            print(number/number2)
            return
        else:
            print('ERROR')
    calc(number,number2)
    quest = input('Do You Want Continue? (Yes/No): ').lower()
    if quest == 'yes' or quest == 'Yes':
        continue
    elif quest == 'no' or quest == 'No':
        print('Good Bye :) ')
        break
    else:
        print('Please Type Yes Or No! \n Good Bye!')
        break