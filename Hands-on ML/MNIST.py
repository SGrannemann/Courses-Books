from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score
mnist = fetch_openml('mnist_784', version=1)


# train test split

X, y =mnist['data'], mnist['target']
y = y.astype(np.uint8)
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
# use kneighbors classifier for baseline

knn_clf = KNeighborsClassifier()
#knn_clf.fit(X_train, y_train)

#knn_clf.predict(X_test)

params = [{'weights': ['uniform'], 'n_neighbors': [1, 5, 10, 100, 1000]}, {'weights': ['distance'], 'n_neighbors': [1, 5, 10, 100, 1000]}]

# start a grid search

#grid_search = GridSearchCV(knn_clf, param_grid=params, scoring='accuracy', cv=3)
#grid_search.fit(X_train, y_train)
#print(grid_search.best_params_)

# distance is optimal, n_neighbors doesnt seem to make a difference
knn_clf = KNeighborsClassifier(weights='distance', n_neighbors=4)

# accuracy should be greater than 97 % (evaluate that)

knn_clf.fit(X_train, y_train)

predictions = knn_clf.predict(X_test)
acc = accuracy_score(y_test, predictions)
print(acc)