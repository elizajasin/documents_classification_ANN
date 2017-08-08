__author__ = 'elizajasin'

import sklearn
from sklearn.neural_network import MLPClassifier

def training(data_features, data_class):
    cls = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10, 10), random_state=1)
    cls = cls.fit(data_features, data_class)
    return cls

def testing(ANN_Model,fe_test,class_test):
    pred = ANN_Model.predict(fe_test)

    actual = []
    prediction = []

    for i in pred:
        prediction.append(i)

    for j in class_test:
        actual.append(j)
    return actual,prediction