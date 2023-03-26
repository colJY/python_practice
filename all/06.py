a = int(input())

while(a >= 30):
   a = int(input('올바른 값을 입력하세요'))
   
for i in range(1,a+1):
    if('3' in str(i) or '6' in str(i) or '9' in str(i)):
        print('X',end=' ')
    else: print(i,end=' ')
