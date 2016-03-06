import time
from datetime import datetime
import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold


print "Script start at ", datetime.now().isoformat()

X=np.load('F:/NYU/Hackathon/numpy_array.npy')
Y=X[:,:3] #patient_id cancer_type tissue_type
X=X[:,3:] #rpm

RS=np.random.RandomState(90)
perm=RS.permutation(678)

Y=Y[perm]
X=X[perm]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y[:,1], test_size=0.25, random_state=30, stratify=Y[:,1])

pipe=Pipeline([('pca',PCA()), ('scaled',StandardScaler()), ('logistic_regression',LogisticRegression())])

pca_val=[1,2,4,13,1046]

C_vals = np.logspace(-9,9, num=19, base=2)

gs=GridSearchCV(pipe, dict(pca__n_components=pca_val, logistic_regression__C=C_vals), cv=10, verbose=100)
gs.fit(X_train, Y_train)

score=gs.score(X_test, Y_test)

print score
print 'best_score'
print gs.best_score_
print 'best_estimator'
print gs.best_estimator_
print 'best_params'
print gs.best_params_

outfile="grid_logisticregression_cancer_search_scores_{0}.out".format(int(time.time()))

with open(outfile, "w") as scoreFile:
    writer = csv.writer(scoreFile, delimiter = ",")
    paramKeys = list(gs.grid_scores_[0].parameters.keys())

    writer.writerow(['mean']+ paramKeys)
    
    for i in gs.grid_scores_:
        output = list()
        output.append(i.mean_validation_score)

        for k in paramKeys:
            output.append(i.parameters.get(k))

        writer.writerow(output)


print "Script end at ", datetime.now().isoformat()