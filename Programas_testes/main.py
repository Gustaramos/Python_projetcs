# cook your dish here
t = int(input())
while t > 0:
    x, y = map(int, input().split())
    if x > y:
        print('Loss')
    if y > x:
        print('Profit')
    if x == y:
        print('Neutral')
    t -= 1