
a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

count = 1

while (count % a != 0 or count % b != 0 or count % c != 0):
    count += 1


print(count)
    




