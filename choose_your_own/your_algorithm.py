#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.ion()
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


from time import time
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import tree

#cls = tree.DecisionTreeClassifier(min_samples_split=40)
cls = SVC(kernel='rbf', C=102764)
#cls = GaussianNB()
#cls = NearestCentroid(metric='euclidean', shrink_threshold=None)

t0 = time()
cls.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
y_pred = cls.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"

from sklearn.metrics import accuracy_score

print "accuracy: ", accuracy_score(labels_test, y_pred)


#try:
prettyPicture(cls, features_test, labels_test)
#except NameError:
#    pass
