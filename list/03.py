a = int(input())

b = list(map(int, (input().split())))
temp = b[0]

for i in range(a-1):
    
    if(b[i+1] >= b[i] and temp >= b[i]):
        temp = b[i]
    elif(b[i+1]<= b[i] and temp >= b[i+1]):
        temp = b[i+1]
    

print(temp)

