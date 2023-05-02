import math
def trigonometry():
    request = (input(f'what trig ratio do you want? SINE,COSINE OR TANGENT? :' ))

    query = int(input('enter value>>:'))        
    if request.lower() == 'sine':
        print(f'vaLue of sine {query}')
        print(f'the answer is:{round(math.sin(query))}')
    elif request.lower() == 'cosine':
        print(f'vaLue of COS {query}')
        print(f'the answer is: {round(math.cos(query))}')
    elif request.lower() == 'tangent':
        print(f'vaLue of tan {query}')
        print(f'the answer is :{round(math.tan(query))}')
 

trigonometry()




