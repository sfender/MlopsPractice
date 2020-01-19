import numpy as np
from sklearn.ensemble import RandomForestClassifier
import sys
import conf
try: import cPickle as pickle   # python2
except: import pickle           # python3

import mlflow
import mlflow.sklearn

if len(sys.argv) != 2:
    sys.stderr.write('Arguments error. Usage:\n')
    sys.stderr.write('\tpython train_model.py INPUT_MATRIX_FILE SEED OUTPUT_MODEL_FILE\n')
    sys.exit(1)

input = conf.train_matrix
output = conf.model
seed = int(sys.argv[1])

with open(input, 'rb') as fd:
    matrix = pickle.load(fd)

labels = np.squeeze(matrix[:, 1].toarray())
x = matrix[:, 2:]

sys.stderr.write('Input matrix size {}\n'.format(matrix.shape))
sys.stderr.write('X matrix size {}\n'.format(x.shape))
sys.stderr.write('Y matrix size {}\n'.format(labels.shape))

n_estimators = 700
n_jobs = 5

clf = RandomForestClassifier(n_estimators=n_estimators, n_jobs=n_jobs, random_state=seed)
clf.fit(x, labels)

mlflow.log_param("n_estimators", n_estimators)
mlflow.log_param("n_jobs", n_jobs)
mlflow.log_param("seed", seed)

with open(output, 'wb') as fd:
    pickle.dump(clf, fd)

