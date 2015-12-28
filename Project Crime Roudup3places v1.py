import folium
import pandas
import os
from pandasql import sqldf

# Determine current absolute path of execution file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#limit number of records if only sample is required
MAX_RECORDS = 10000000000

#define where the map will be centered
SF_COORDINATES = (37.76, -122.45)

#read in the San Francisco crime dataset for 2015 incidents
crimedata = pandas.read_csv('SFPDIncidents2015.csv')

#create map with San Francisco zoomed in   
SFmap = folium.Map(location=SF_COORDINATES, zoom_start=14)

#SQL statement that will round the x and y geocode coordinates, filter by most
#dangerous crimes, and group by the top geocodes
SQLGroupByQuery = """
select round(X,3) X, round(Y,3) Y, count(*) from crimedata
where Category in ("ASSAULT","SEX OFFENSES FORCIBLE","KIDNAPPING")
group by round(X,3) || round(Y,3)
having count(*) > 28
order by count(*) desc
;
"""

#capture results of the grouping and rounding SQL statement
highCrimeArea = sqldf(SQLGroupByQuery, globals())
print highCrimeArea

#SQL statement that will filter incidents by most dangerous crimes
SQLDetailFilterQuery = """
select X,Y from crimedata
where Category in ("ASSAULT","SEX OFFENSES FORCIBLE","KIDNAPPING")
;
"""

#capture results of the filtering SQL statement
individualDangerousCrime = sqldf(SQLDetailFilterQuery, globals())

#add a marker for every rounded number
for each in highCrimeArea[0:32].iterrows():
  SFmap.circle_marker(
  location = [each[1]['Y'],each[1]['X']],
  radius = 200,
  fill_color = 'red',
  line_color = 'red',
  fill_opacity = .6)
  
#add a marker for detail crime incident (use a subset defined by max records)
for each in individualDangerousCrime[0:MAX_RECORDS].iterrows():
 SFmap.circle_marker(
 location = [each[1]['Y'],each[1]['X']],
 radius = 10,
 fill_color = 'white',
 fill_opacity = 1)

#create static HTML file that contains map with plotted markers
SFmap.create_map(path='SFCrimeMapRound3Places.html')