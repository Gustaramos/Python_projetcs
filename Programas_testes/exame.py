t = int(input())
for tc in range(t):
    x, y, a = map(int, input().split())
    if a >= x:
        if a < y:
            print('YES')
        else:
            print('NO')
    elif a < y:
        print("NO")