Installation Instructions:

a.	Environment, Installation and Datasets 

	The environment utilized was Canopy for Python. The only non-standard package utilized was Folium. 
	The following installation script is necessary to install Folium into the Canopy environment. 
	   i.	$pip install folium

	The following package is necessary to utilize DBSCAN in the modified example module.
	   ii.	Go to Canopy Package Manager and add scikit_learn 0.17-1

	The input file should be placed in the same directory as where the Python program is run. 
	The same dataset (SFPDIncidents2015.csv) is utilized for all runs.

	The main program to run is the Project Crime Roundup2places v1.py. 
	This will produce the HTML file SFCrimeMapRound2Places.html which is a dynamic map of the results. 
	The resulting HTML file will be in the same directory as the program.

	The other programs are available if the exploratory programs want to be run also. 
	They will behave the same as the main program mentioned above, except they might also produce a pop-up graph.
	

File Manifest:

Project Write-up: 
Project Walt Arp v1d.docx

Input File For all Software Runs: 
SFPDIncidents2015.csv

Exploratory code to determine methodology: 
Project Crime Kmeans.py

Exploratory code HTML map result: 
TestKmeanCrimeMap.html

Geo-Code Rounded to 3 decimal places:		
Project Crime Roundup3places v1.py

3 decimal places HTML map result: 
SFCrimeMapRound3Places.html

Geo-Code Rounded to 2 decimal places:		
Project Crime Roundup2places v1.py

2 decimal places HTML map result: 
SFCrimeMapRound2Places.html

Modified DBScan Sample Code:		
Project Crime DBScan.py

DBScan HTML map result: 
DBSCANCrimeMaps.html
