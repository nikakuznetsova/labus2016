__author__ = 'student'
A=[1, 2, 3, 4, 5]
for i in range(0, len(A), 2):
    A.insert(i+1, A.pop(i))
print(A)