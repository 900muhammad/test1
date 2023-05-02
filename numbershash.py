import hashlib,string
def hashGiver(string1):
    bits = bytes(string1,'utf-8')
    return bits


string1 = str(input('Enter a word/sentence:>'))
password = hashGiver(string1)
print(password)



