print('1  2  3  4  5  6  7  8  9  10  11   12')
print('--------------------------------------')
for x in range(1,13):
    print(str(x).rjust(1),end=' ')
    print('|',end='')
    for x2 in range(1,13):
        print(str(int(x) + int(x)).rjust(1),end='')
    print()

