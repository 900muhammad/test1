import random #Random Generator
dates = range(2004,2024)
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept', 'Oct','Nov','Dec']
days = range(1,32)
for x in range(0,6):
    print(random.choice(days),random.choice(months),random.choice(dates))
#a random birthday generartor
