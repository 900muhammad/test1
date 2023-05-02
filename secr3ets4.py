import secrets,string
def aLpha_numeric_code(length):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for x in range(length))
    return password


length = int(input('ENTER A VALUE>>'))
code   = aLpha_numeric_code(length)
print(f' Your Code is>> {code}')




    
