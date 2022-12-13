for t in range(int(input())):
    a, c = map(int, input().split())
    b = c - a
    if b % 2 == 0:
        print(int(a + (b/2)))
    else:
        print(-1)
    t -= 1