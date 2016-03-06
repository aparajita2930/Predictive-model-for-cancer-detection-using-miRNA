import time
from datetime import datetime
import csv
import numpy as np
from sklearn.cluster import KMeans
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

p=PCA(n_components=0.5).fit(X_train)
print(p.explained_variance_)
