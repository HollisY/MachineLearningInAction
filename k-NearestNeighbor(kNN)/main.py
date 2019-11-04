import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import array

# # step one: movie
# group, labels = kNN.createDataSet()
# res = kNN.classify0([1, 9], group, labels, 3)
# print(res)

# # step two: dating
# datingDataMat, datingLabels = kNN.file2matrix('./datingTestSet2.txt')
# fig = plt.figure()
# plt.xlabel('travel')
# plt.ylabel('play')
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
# plt.show()

# kNN.datingClassTest()

# # predict dating
# kNN.classifyPerson()

# predict handwriting
kNN.handwritingClassTest()