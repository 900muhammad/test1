import random
def passwordGen():
    while True:
      request = input('do you need a password?:')
      letters =  ('a''b''c''d''e''f''g''i''j''k''l''m''n''o'
               'p''q''r''s''t''u''v''w''x''y''z')
      symbols = ['@','#','$','!','%','?',"*","@@#$%"]
      numbers =  range(287,10000)
      if request.lower() == 'yes':
        print('ok,here are your passwords:')
        for x in range(0,9):
              print(f'{random.choice(letters)}{random.choice(numbers)}{random.choice(symbols)}')
      elif  request.lower != 'yes':
                      print('generate yours here:')
                      print(f'MY PASSWORD:{input(">>")}')
   

passwordGen()
        