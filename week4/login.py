from random import randint
print('Welcome To System \n Request Login!')
# quest = input('What Do You Want? \n Login/Register').capitalize()
# reglogin = input('Login : ')
global login_checker
global generate_password
logins1 = []
passw1 = []
def login_checker():
      for check in logins1:
            qlogin = input('Please Type Your Login: ')
            if qlogin in check:
                  for chppass in passw1:
                        cpass = input('Please Type Password :')
                        if cpass in chppass:
                              print("success")
                        else:
                              print('Invalid Password Please Try Again')
                        
                        
            else:
                  print("Invalid Login Please Try Again ")
                  continue

def generate_password():
        global passw
        global logins
        pas = ''
        reglogin = input('Login : ')
        for i in range(7):
            password = randint(0,10)
            pas += str(password)
        result = reglogin+pas
        print(f'Success Registred Account :) \n Your Login: {reglogin}\nYour Password: {result}')
        passw = result.split()
        logins = reglogin.split()

quest = input('What Do You Want?(Register/Login): ').lower()
if quest == 'login':
      login_checker()

elif quest == 'register':
      generate_password()
      passw1.extend(passw)
      logins1.extend(logins)
      print(passw1)
      print(logins1)
      b = input('Do You Want Login? (Yes/No):').lower()
      if b == 'yes':
            login_checker()
      else: print('Invaild Type Try Again! ')
else: print('Invalid Type !')