a = int(input())

list = input().split()

e_list = []
for i in range(24):
    e_list.append(0)

for i in range(a):
    list[i] = int(list[i])

for i in range(a):
    e_list[list[i]] += 1
    
for i in range(1, 24):
    print(f'{e_list[i]} ',end='')


