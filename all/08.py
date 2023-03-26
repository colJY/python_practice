h,b,c,s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

while(h>48000 and b >32 and b%8 != 0 and s>6000):
    h,b,c,s = input().split()

sound = h*b*c*s/8/1024/1024
print(f'{sound:.1f} MB')