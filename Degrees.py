import math
def FindDegree():
    print('''This function converts integers to degree
 and also converts from degrees to radians''')
    value = int(input('Enter a value>>'))
    print(f'{value} in degree = {math.degrees(value)} degrees')
    print(f'The equivalent in radians = {math.radians(value)} rads')

    


FindDegree()

