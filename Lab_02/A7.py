a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a + b) % 2 == (c + d) % 2:
    print('YES')
    if (a + b) % 2 == 0:
        print('White')
    else:
        print('Black')
else:
    print('NO')