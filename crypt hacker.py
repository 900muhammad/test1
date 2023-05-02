print('encrypted cipher to hack')
message = input('>>')
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(SYMBOLS)):
    decrpyted = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(SYMBOLS)
                decrpyted = decrpyted + SYMBOLS[num]
            else:
                decrpyted = decrpyted + symbol
print('Key #{}:{}'.format(key , decrpyted))