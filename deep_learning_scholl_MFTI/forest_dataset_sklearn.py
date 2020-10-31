import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score, mean_squared_error, make_scorer
from sklearn.neighbors import DistanceMetric


all_data = pd.read_csv('forest_dataset.csv')
#print(all_data.head())
'''
print(all_data.shape)

labels = all_data[all_data.columns[-1]].values
feature_matrix = all_data[all_data.columns[:-1]].values

train_feature_matrix, test_feature_matrix, train_labels, test_labels = train_test_split(
    feature_matrix, labels, test_size=0.2, random_state=42)

# �������� ������ � ��������� �������������� C
clf = LogisticRegression(C=1)
# �������� ������
clf.fit(train_feature_matrix, train_labels)
# ������������ �� �������� �������
y_pred = clf.predict(test_feature_matrix)

print(accuracy_score(test_labels, y_pred))

# ������ �������� ������, ������ ������
clf = LogisticRegression(solver='saga')

# ������ �����, �� ������� ����� ������
param_grid = {
    'C': np.arange(1, 5), # ����� ����� ������� ������� ������, [1, 2, 3, 4]
    'penalty': ['l1', 'l2'],
}

# �������� ������ GridSearchCV
search = GridSearchCV(clf, param_grid, n_jobs=-1, cv=5, refit=True, scoring='accuracy')

# �������� �����
search.fit(feature_matrix, labels)

# ������� ��������� ���������
print(search.best_params_)
'''

labels = all_data[all_data.columns[-1]].values
feature_matrix = all_data[all_data.columns[:-1]].values

#�������� ��������
train_feature_matrix, test_feature_matrix, train_labels, test_labels = train_test_split(
    feature_matrix, labels, test_size=0.2, random_state=42)

# �������� ������
clf = KNeighborsClassifier(weights='distance', metric='manhattan')
# �������� ������
clf.fit(train_feature_matrix, train_labels)
# ������������ �� �������� �������
y_pred = clf.predict(test_feature_matrix)

print(accuracy_score(test_labels, y_pred))

gbr_grid_search = GridSearchCV(clf, 
                               [{'n_neighbors': np.arange(1,10)}],
                               cv=5,
                               
                               scoring='accuracy',
                               n_jobs=-1)

gbr_grid_search.fit(train_feature_matrix, train_labels)

print(gbr_grid_search.best_params_)
print(gbr_grid_search.best_score_)
print(gbr_grid_search.best_estimator_)