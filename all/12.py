a, d, n = input().split()

a = int(a)
d = int(d)
n = int(n)
z = 0

for i in range(n):
    if(i == 0):
        z = a
    else:
        z = z+d

print(z)