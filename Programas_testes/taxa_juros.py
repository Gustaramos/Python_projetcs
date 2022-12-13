# interest rate X percent per annum
# inflation Y percent per annum

t = int(input())

while t > 0:
    x, y = map(int, input().split()) 
    if x >= y * 2:
        print('YES')
    else:
        print('NO')
    t -= 1