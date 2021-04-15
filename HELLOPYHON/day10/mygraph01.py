import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymysql
 
conn = pymysql.connect(host='localhost', port=3336, user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()


# make 3d axes
fig = plt.figure() 
ax = fig.gca(projection='3d')

# test data
x = np.array([0,0,0,0,0])
# x = np.arange(-10., 10., 1)
y = np.array([0,1,2,3,4])
# y = np.arange(-10., 10., 1)

print(x)
print(y)

z1 = np.array([2,3,4,2,2])
# z1 = x + y
# z2 = x * x
# z3 = -y * y

# plot test data
ax.plot(x, y, z1)
ax.plot(x+1, y, z1)
ax.plot(x+2, y, z1)
# ax.plot(x, y, z2)
# ax.plot(x, y, z3)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()