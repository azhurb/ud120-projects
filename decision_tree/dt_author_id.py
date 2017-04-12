#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

min_samples_split=40

print "min_samples_split: ", min_samples_split

print "number of features: ",len(features_train[0])
exit

from sklearn import tree
cls = tree.DecisionTreeClassifier(min_samples_split=min_samples_split)

t0 = time()
cls.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
y_pred = cls.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"

#authors = ["Sara", "Chris"]

#print "element 10: ", y_pred[10], " - ", authors[y_pred[10]]
#print "element 26: ", y_pred[26], " - ", authors[y_pred[26]]
#print "element 50: ", y_pred[50], " - ", authors[y_pred[50]]

#print "Cris emails: ", sum(y_pred)

from sklearn.metrics import accuracy_score

print "accuracy: ", accuracy_score(labels_test, y_pred)


#########################################################


