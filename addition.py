import math
def addition():
    print('More Maths Functions')
    sum = int(input('enter the first value>>'))
    sum2 = int(input('enter the second value>>'))
    print('The Result Is:')
    print(math.sqrt(sum) + math.sqrt(sum2))
    print('Do you need to convert to degree/radians')
    reply = input('yes/no >>')
    if reply.lower() == 'yes':
      print('Converting to Degrees.....')
      print(math.degrees(sum) and math.degrees(sum2))
    elif reply.lower() == 'no':
       print('Exit')
    


addition()