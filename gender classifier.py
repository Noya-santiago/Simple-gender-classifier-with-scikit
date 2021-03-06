from sklearn import tree

X = [[181,80,44], [177,70,43],[160,60,38],[154,54,37],
     [160,65,40],[190,90,45],[175,64,39],[177,70,40],[159,55,37],
     [171,75,42],[181,85,43]]

Y = ['male','female','female','female','female','male',
     'female','female','female', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[155,55,34]])

print(prediction)