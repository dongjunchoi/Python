import numpy as np

a = [1,2,3,4,5,6,7,8]
print(a)


b = np.reshape(a,(2,4))
print(b)
print(b[1][2])
print(b[1,2])
c = np.reshape(a,(4,2))

d = [
        [1,2,3,4],[5,6,7,8]
    ]
print(d[1][2])

# print(b)
# print('\n')
# print(c)