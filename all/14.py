a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

cal = 0

for i in range(n):
    if(i == 0):
        cal = a
    else : cal = cal*m+d

print(cal)