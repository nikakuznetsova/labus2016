__author__ = 'student'
import random
random.seed(0)
N=int(input())
I=0
for i in range (1,N):
    a=random.uniform(-3, 3)
    if -2<=a<=2:
        f=-a**2+4
    else:
        f=0
    I+=f
I=((3+3)/N)*I
print(I)
