__author__ = 'elizajasin'

import numpy as np
from sklearn import metrics
from sklearn import model_selection as m_eval

def kfold_CV(classifier, df, dc, n_fold):
    k_fold = m_eval.KFold(n_splits=n_fold)
    folds = m_eval.cross_val_score(classifier,
                                   df,
                                   dc,
                                   cv=k_fold)
    mean_folds = np.mean(folds)
    return folds, mean_folds

def evaluasi(actual, prediction):
    print(metrics.classification_report(actual,prediction))