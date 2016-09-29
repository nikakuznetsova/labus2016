__author__ = 'student'
A=[1, 2, 3, 4, 2]
t=int(input())
for i in range(t):
    m=A.pop(-1)
    A.insert(-m,m)
print(A)