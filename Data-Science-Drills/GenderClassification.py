#Gender classificator built with scikit learn
from sklearn import tree

#[height, weight, shoe size]
x = [[190, 80, 30], [186, 82, 29], [148, 41, 23],
    [173, 61, 28,], [167, 55, 24], [156, 40, 23],
    [182, 76, 26]]

y = ['male','male','female','male','female','female','male']

#Creation of the decision tree
clf = tree.DecisionTreeClassifier()

#Fitting with the data
clf.fit(x,y)

prediction = clf.predict([[175, 60, 28]])
print(prediction)
