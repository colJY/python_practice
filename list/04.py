a = int(input())
i = 0
b = []
c = []



for i in range(19):
   
   c.append([])
   for q in range(19):
      c[i].append(0)

for i in range(a):
   x, y = list(map(int,(input().split())))
   c[x-1][y-1]= 1

for i in range(19):
   if(i != 0 ):
    print()
   for q in range(19):
    print(c[i][q],end=' ') 


   




