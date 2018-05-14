# coding=utf-8

# sklearn中为我们准备的数据-iris
# iris有三种鸢尾花，山鸢尾花，变色鸢尾和维吉尼亚鸢尾
# 数据中有4个特征（feature）
# sepal length (花萼长度)
# sepal width (花萼宽度)
# petal lenth (花瓣长度)
# petal width (花瓣宽度)

from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
# 获取鸢尾数据
iris = load_iris()

# 用来做测试的数据下标
test_idx = [0,50,100]

# 用以训练的数据
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis=0)

# 用以测试的数据
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]


# 决策树
clf = tree.DecisionTreeClassifier(criterion='entropy',splitter='best',min_samples_split=5)
clf.fit(train_data,train_target)

# 打印出测试数据和决策树的预言数据
# 结果应该是一样的（即决策树能正确预测）
print "test_target:"
print test_target
print "predict:"
print clf.predict(test_data)


# 将决策树可视化
# 需要pydot(我安装了兼容版本pydotplus)
# 同时需要Graphviz(请去官网www.graphviz.org下载)
from sklearn.externals.six import StringIO
import pydotplus
#通过调用graphviz的相关函数，输出决策树图像
dot_data = StringIO()
tree.export_graphviz(clf,
                        out_file=dot_data,
                        feature_names=iris.feature_names,
                        class_names=iris.target_names,
                        filled=True,rounded=True,
                        impurity=True)


graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# 输出pdf，显示整个决策树的思维过程
graph.write_pdf("viz4.pdf")