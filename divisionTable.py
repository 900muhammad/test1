print(' 1   2   3   4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20')
print('-----------------------------------------------------------------')
for x in range(1,21):
    print(str(x).rjust(2), end = ' ' )
    print('|',end = ' ')
    for x2 in range(1,21):
        print(str(x // x2).rjust(2), end =' ')
    print()