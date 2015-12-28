#Demo of DBSCAN clustering algorithm. (n.d.). Retrieved December 3, 2015, 
#from http://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#example-cluster-plot-dbscan-py 
#Code created by scikit-learn.org, except as noted (see Walt Begin and Walt End for code inserted into the original program). 

print(__doc__)

import numpy as np 
import os

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

# Determine current absolute path of execution file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1], [.2, .4]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.2,
                            random_state=0)

X = StandardScaler().fit_transform(X)
### Modified Sample Code by Walt Begin ########################################
import pandas 
import folium
from numpy import vstack

#define where the map will be centered
SF_COORDINATES = (37.76, -122.45)

#create map with San Francisco zoomed in 
SFmap = folium.Map(location=SF_COORDINATES, zoom_start=13)

#for sample testing purposes
MAX_RECORDS = 750

X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.2,
                            random_state=0)
X = StandardScaler().fit_transform(X)

#read in the San Francisco crime dataset for 2015 incidents
crimedata = pandas.read_csv('SFPDIncidents2015.csv')

#read the geocode coordinates into a list
totalGeoCoordinateList = []
for each in crimedata[0:MAX_RECORDS].iterrows():
 myList=[each[1]['X'],each[1]['Y']]
 totalGeoCoordinateList.append(myList)

#put list into vertically stacked array
X = vstack((totalGeoCoordinateList))

# Compute DBSCAN
#db = DBSCAN(eps=0.3, min_samples=10).fit(X)
db = DBSCAN(eps=0.014, min_samples=100).fit(X)
 
### Modified Sample Code by Walt End ##########################################

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)

core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))

# Plot result
import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]

    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
### Modified Sample Code by Walt Begin ########################################
            
    #add a marker for DBSCAN cluster point to map
    if k == -1:
        #add a marker for DBSCAN cluster point to map
        for each in xy[0:1000]:
            SFmap.circle_marker(
            location = [each[1],each[0]],
            radius = 25,
            fill_color = 'white',
            fill_opacity = .7)
    else:   
        for each in xy[0:1000]:
            SFmap.circle_marker(
            location = [each[1],each[0]],
            radius = 300,
            fill_color = 'red',
            fill_opacity = .3)
      
    xy = X[class_member_mask & ~core_samples_mask]

    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)
                     
    #add a marker for DBSCAN cluster point to map
    if k == -1:
        #add a marker for DBSCAN cluster point to map
        for each in xy[0:1000]:
            SFmap.circle_marker(
            location = [each[1],each[0]],
            radius = 25,
            fill_color = 'white',
            fill_opacity = .7)
    else:   
        for each in xy[0:1000]:
            SFmap.circle_marker(
            location = [each[1],each[0]],
            radius = 130,
            fill_color = 'red',
            fill_opacity = .3)
      
#create static HTML file that contains map with plotted DBSCAN clusters
SFmap.create_map(path='DBSCANCrimeMap.html')

### Modified Sample Code by Walt End ########################################## 
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()