a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

z = 0

for i in range(n):
    if(i == 0):
        z = a
    else:
        z = z*r

print(z)
