import secrets
def HardBits():
    print('''This generates bytes tokens for companies''')
    print('PLease enter a number')
    bits = int(input('Enter the an amount of bytes>'))
    print(f'GENERATING.......{bits} bytes of tokens')
    print(f'===Generated {bits} of bytes===')     
    for x in range(bits):
        print(secrets.token_bytes(bits))     
    print(f'The hex tokens :{bits} tokens produced'.center( 20 ,'='))
    for x in range(bits):
        print(f'--|{secrets.token_hex(bits)}|--')
    print(f'{bits} ===SAFE URLS===')
    for x in range(bits):
        print(f'--|={secrets.token_urlsafe(bits)}=|--')


HardBits()