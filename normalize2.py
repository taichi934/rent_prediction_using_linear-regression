import numpy as np


# x = np.array([
#     [10, 10, 10, 10, 10, 10, 13, 13, 13, 5, 10, 10, 10, 10,
#         10, 9, 9, 4, 4, 7, 7, 7, 7, 7, 7, 12, 13, 13, 15],
#     [20.7, 20.7, 20.7, 20.7, 41.4, 20.7, 25.21, 52.36, 25.63, 22.85, 12.5, 12.5, 12, 12, 12, 20.79, 21.88, 11.28, 12.73, 31.7, 25.1, 25.06, 25.1, 25.06, 25.1, 23, 52.36, 25.63, 21.18]])

x1 = np.array([10, 10, 10, 10, 10, 10, 13, 13, 13, 5, 10, 10, 10,
               10, 10, 9, 9, 4, 4, 7, 7, 7, 7, 7, 7, 12, 13, 13, 15])
x2 = np.array([20.7, 20.7, 20.7, 20.7, 41.4, 20.7, 25.21, 52.36, 25.63, 22.85, 12.5, 12.5, 12, 12,
               12, 20.79, 21.88, 11.28, 12.73, 31.7, 25.1, 25.06, 25.1, 25.06, 25.1, 23, 52.36, 25.63, 21.18])

y = np.array([88500, 86700, 87300, 88200, 170000, 83000, 100000, 170000, 105000, 83000, 56000, 65000, 56000, 63000,
              67000, 87000, 85000, 64000, 67000, 140000, 113000, 117000, 113000, 110000, 114000, 87000, 170000, 105000, 78000])


sx1 = (x1-np.mean(x1))/np.std(x1)
sx2 = (x2-np.mean(x2))/np.std(x2)
sx = np.array([sx1, sx2])

sy = (y-np.mean(y))/np.std(y)

sx = np.append(sx, np.ones([1, sx.shape[1]]), axis=0)
sxsx = np.matmul(sx, sx.T)
sxsy = np.matmul(sx, sy)

sw = np.matmul(np.linalg.inv(sxsx), sxsy)

print(sw)

# x = np.append(x, np.ones([1, x.shape[1]]), axis=0)
# xx = np.matmul(x, x.T)
# w = np.matmul(np.linalg.inv(xx), xy)
