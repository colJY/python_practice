a = int(input())
b = 0

while(a > 100000000):
    a = int(input('정확한 값을 입력하세요'))


for count in range(1,a+1):
    
    b = count + b 
    if(b>=a):
        break
    
print(b)

