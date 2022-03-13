import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data plots
co_pts = pd.read_csv('random-test-data.csv')
df = co_pts.to_numpy()
x = df[:, 0]
y = df[:, 1]
# number of cluster centers
# K = 3


# plt.scatter(x, y, marker='o', c='k', s=2)
# plt.axis([0, 10, 0, 10])
# plt.axis('square')
# plt.grid(True)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

dist_tensor = np.empty([len(x), len(y)])
for i in range(0, len(x)):
    for j in range(0, len(y)):
        dist_tensor[i, j] = np.sqrt(np.square(x[i] - x[j]) + np.square(y[i] - y[j]))

dist_arr = dist_tensor.flatten()
dist_arr = np.sort(dist_arr)
print(dist_arr[-2980:3000])
# idx1 = np.where(dist_tensor == dist_arr[-1])
# idx2 = np.where(dist_tensor == dist_arr[-2])
# idx3 = np.where(dist_tensor == dist_arr[-3])

# print(idx1, end=" ")
# print(idx2, end=" ")
# print(idx3)
# cluster_1 = np.empty([3000, 2])
# cluster_2 = np.empty([3000, 2])
# cluster_3 = np.empty([3000, 2])
#
# for j in range(0, len(y)):
#     d1 = np.sqrt(np.square(x[2998] - x[j]) + np.square(y[2998] - y[j]))
#     d2 = np.sqrt(np.square(x[2997] - x[j]) + np.square(y[2997] - y[j]))
#     d3 = np.sqrt(np.square(x[2999] - x[j]) + np.square(y[2999] - y[j]))
#     if (d1 >= d2) & (d1 >= d3):
#         cluster_1[j, 0] = x[j]
#         cluster_1[j, 1] = y[j]
#     elif (d2 >= d1) & (d2 >= d3):
#         cluster_2[j, 0] = x[j]
#         cluster_2[j, 1] = y[j]
#     else:
#         cluster_3[j, 0] = x[j]
#         cluster_3[j, 1] = y[j]
#
# plt.scatter(cluster_1[:, 0], cluster_1[:, 1], marker='o', c='y', s=2)
# plt.scatter(cluster_2[:, 0], cluster_2[:, 1], marker='o', c='r', s=2)
# plt.scatter(cluster_3[:, 0], cluster_3[:, 1], marker='o', c='b', s=2)
#
# plt.axis([0, 10, 0, 10])
# plt.axis('square')
# plt.grid(True)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()