t = int(input())
for i in range(t):
    x, n = map(int, input().split())
    r = int((x / 10) * n)
    print(r)