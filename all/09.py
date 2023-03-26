w,h,b = input().split()

w = int(w)
h = int(h)
b = int(b)

file = w*h*b/8/1024/1024

print(f'{file:.2f} MB')