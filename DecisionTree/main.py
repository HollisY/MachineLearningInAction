import trees
import treePlotter

# myDat, labels = trees.createDataSet()
# print(labels)
# myTree = treePlotter.retrieveTree(0)
# print(myTree)
# print(trees.classify(myTree, labels, [1, 0]))
# print(trees.classify(myTree, labels, [1, 1]))
# # # print(trees.chooseBestFeatureToSplit(myDat))
# # print(myTree)

# # print(treePlotter.retrieveTree(1))
# # myTree = treePlotter.retrieveTree(0)
# # treePlotter.createPlot(myTree)

# trees.storeTree(myTree, 'classifierStorage.txt')
# trees.grabTree('classifierStorage.txt')

# 隐形眼镜
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses, lensesLabels)
print(lensesTree)
treePlotter.createPlot(lensesTree)