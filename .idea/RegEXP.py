import re
phoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
find = phoneNum.search('My digits are 456-345-456')
print('REG FOUND THE NUMBER:'+ find.group())
heroRegex = re.compile(r'Batman|Tinafey')
find2 = heroRegex.search('The Batman has arrived tina fey')
print(find2.group())
batREGEX = re.compile(r'Bat(man|mobile|car|cave)'.lower())
fetch = batREGEX.search('THe Batmobile lost batman') 
print(fetch.group().lower())
batREGEX = re.compile(r'Bat(wo)?man')
fetch = batREGEX.search('Red man and Batman ')
print(fetch.group())

