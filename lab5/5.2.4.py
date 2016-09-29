__author__ = 'student'
A=[1, 2, 2, 3]
b=0
for i in range(len(A)):
    if A.count(A[i])>b:
        b=A.count(A[i])
print(b)

