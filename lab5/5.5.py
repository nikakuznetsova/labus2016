__author__ = 'student'
k=int(input())
n=int(input())
A=[]
for i in range(0, k):
    A.append(1)
for l in range(k, n+1):
    A.append(A[l-1]+A[l-2]+A[l-3])
print(A[len(l-1)])
