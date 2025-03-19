import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

df = pd.read_csv('iris.csv')
X = df.loc[:, ['petal_length', 'petal_width']].values
species = df['species'].unique()

wcss = []

for i in range(1, 10):
  model = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
  model.fit(X)
  wcss.append(model.inertia_)

plt.plot(range(1, 10), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

model = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
y_kmeans = model.fit_predict(X)
y_kmeans = np.where(y_kmeans < 2, 1 - y_kmeans, y_kmeans)

y_species = np.array([species[i] for i in y_kmeans])
cross_tab = pd.crosstab(df['species'], y_species)
print(cross_tab)

for i in range(3):
  plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s = 100, label = str(i) + '-' + species[i])
    
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of plants')
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.legend()
plt.show()

cluster_centers = [X[model.labels_ == i].mean(axis=0) for i in range(3)]

clusterwise_sse = [0, 0, 0]
for point, label in zip(X, model.labels_):
  clusterwise_sse[label] += np.square(point - cluster_centers[label]).sum()
clusterwise_sse[0], clusterwise_sse[1] = clusterwise_sse[1], clusterwise_sse[0]

for i in range(3):
  print(species[i], 'SSE:', clusterwise_sse[i])
