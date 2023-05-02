import random
def randomBytes():
 while True:
    print('Do you need random bytes code?')
    response = input('Enter yes / no:')
    request = int(input('Enter Amount to generate>>'))
    if response.lower() == 'yes':
        print(f'Generating {request} byte codes')
        for x in range(request):
           print(random.randbytes(request))
    elif response.lower() != 'yes':
       print('Cant generate bytes for you!')
    
    
    

randomBytes()

