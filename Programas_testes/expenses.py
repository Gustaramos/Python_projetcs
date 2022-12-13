t = int(input())
for tc in range(t):
    n, x = map(int, input().split())
    i = 2 ** x
    while n > 0:
        i = int(i/2)
        n -= 1
    print(i)