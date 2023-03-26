b = int(input())
a = list(map(int,input().split()))

for i in range(b-1, -1, -1):
    print(f'{a[i]} ',end='')
