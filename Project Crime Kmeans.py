import folium
import pandas 
import os
from pylab import plot,show
from numpy import vstack
from scipy.cluster.vq import kmeans,vq

# Determine current absolute path of execution file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#limit number of records if only sample is required
MAX_RECORDS = 3000

#define where the map will be centered
SF_COORDINATES = (37.76, -122.45)

#read in the San Francisco crime dataset for 2015 incidents
crimedata = pandas.read_csv('SFPDIncidents2015.csv')

#create map with San Francisco zoomed in 
SFmap = folium.Map(location=SF_COORDINATES, zoom_start=13)

#read the geocode coordinates into a list
totalGeoCoordinateList = []
for each in crimedata[0:MAX_RECORDS].iterrows():
 myList=[each[1]['X'],each[1]['Y']]
 totalGeoCoordinateList.append(myList)

#put list into vertically stacked array
totalGeoCoordinateArray = vstack((totalGeoCoordinateList))

#apply the kmeans function to find centroids 
crimeCentroids,_ = kmeans(totalGeoCoordinateArray,10)

#identify index for each centroid 
idx,_ = vq(totalGeoCoordinateArray,crimeCentroids)

#print centroids
#print idx

#plot the detail points on graph
plot(totalGeoCoordinateArray[idx==0,0],totalGeoCoordinateArray[idx==0,1],'ob',
totalGeoCoordinateArray[idx==1,0],totalGeoCoordinateArray[idx==1,1],'or',
totalGeoCoordinateArray[idx==2,0],totalGeoCoordinateArray[idx==2,1],'oy',
totalGeoCoordinateArray[idx==3,0],totalGeoCoordinateArray[idx==3,1],'oc',
totalGeoCoordinateArray[idx==4,0],totalGeoCoordinateArray[idx==4,1],'om',
totalGeoCoordinateArray[idx==5,0],totalGeoCoordinateArray[idx==5,1],'ok',
totalGeoCoordinateArray[idx==6,0],totalGeoCoordinateArray[idx==6,1],'sr',
totalGeoCoordinateArray[idx==7,0],totalGeoCoordinateArray[idx==7,1],'sy',
totalGeoCoordinateArray[idx==8,0],totalGeoCoordinateArray[idx==8,1],'sc',
totalGeoCoordinateArray[idx==9,0],totalGeoCoordinateArray[idx==9,1],'sm',
totalGeoCoordinateArray[idx==10,0],totalGeoCoordinateArray[idx==10,1],'sk')

#plot the centroid points on graph
plot(crimeCentroids[:,0],crimeCentroids[:,1],'sg',markersize=15)
show()

#add a marker for centroid cluster to map
for each in crimeCentroids[0:10]:
 SFmap.circle_marker(
 location = [each[1],each[0]],
 radius = 500,
 fill_color = 'red',
 fill_opacity = .2)

#add a marker for every event to map (use a subset defined by max records)
for each in crimedata[0:MAX_RECORDS].iterrows():
 SFmap.circle_marker(
 location = [each[1]['Y'],each[1]['X']],
 radius = 10,
 fill_color = 'white',
 fill_opacity = 1)

#create static HTML file that contains map with plotted centroid and detail markers
SFmap.create_map(path='TestKmeanCrimeMap.html')