import random
def weatherForecast():
    request = input('PLEASE ENTER THE WEATHER IN WORDS:')
    weatherINwords = ['windy', ' sunny','stormy']
    if request == weatherINwords[0]:
            print(weatherINwords[0])
            print(random.randint(0,100))
    elif request == weatherINwords[1]:
            print(weatherINwords[1])
            print(random.randint(0,100))
    elif request == weatherINwords[2]:
            print(weatherINwords[2])
            print(random.randint(0,100))
    

weatherForecast()



    