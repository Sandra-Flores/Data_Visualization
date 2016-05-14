
'''
Members: Sandra Flores
		 Alexander Morales
		 Regie Daquioag

Summary: Our project is using the Instagram API to access the popular images on instagram 
		 and using the latitude and longitude from the picures to plot the location on the google map using 
		 the Google Maps API.

'''

#library for HTML
from lxml import etree
#library to read in the url data
import urllib
#library to access the web
import webbrowser, os.path

#################################################################################################
############################### metadata ########################################################


coordinates = "["

for x in range(0,10):


	URLInfo = urllib.urlopen("https://api.instagram.com/v1/media/popular?access_token=3132861916.1677ed0.93a9d071ab1b4659b7cf46905bf5ebe8").read() 

	Index = 0

	while(URLInfo.find("latitude", Index) > 0):

			##################################
			####### Latitude #################

			# finds the latitude
			latIndex = URLInfo.find("latitude", Index)
			latIndex = latIndex + 10

			# will make the next search continue where the last one was found
			Index = latIndex

	
			# empty string to add the latitude into type string
			latCoordinate = "["

			#add the latitude location to the variable latCoordinate
			while (URLInfo[latIndex] != ','):
		
					latCoordinate += URLInfo[latIndex]
					latIndex = latIndex + 1
		
			latCoordinate += ","
	
			coordinates += latCoordinate
	
	
			###################################
			########### longitude #############

			# finds the longitude index
			lonIndex = URLInfo.find("longitude", Index)
			lonIndex = lonIndex + 11
	
			# empty longitude to add the longitude of type string
			lonCoordinate = ""

			#add the longitude location as a string to the variable lonCoordinate
			while (URLInfo[lonIndex] != ','):

					lonCoordinate += URLInfo[lonIndex]
					lonIndex = lonIndex + 1
	
			lonCoordinate += "],"

			coordinates += lonCoordinate
			

coordinates += "];"

print coordinates

######################################################################################################
##################################### HTML / Javascript ##############################################


'''(COMMENT)creates an html file from a given string,
and call the default web browser to display the file.'''

contents = '''
<!DOCTYPE html>
<html> 
<head> 
  <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> 
  <title>map</title> 
  <script src="http://maps.google.com/maps/api/js?sensor=false" 
          type="text/javascript"></script>
  <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
  </style>                
</head> 
<body>
    <div id="map"></div>
  <script type="text/javascript">
  
    var locations = 
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: new google.maps.LatLng(38.94,-95.977),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    var infowindow = new google.maps.InfoWindow();
    var marker, i;
    for (i = 0; i < locations.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][0], locations[i][1]),
        map: map
      });
      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    
    }
    
  </script>
</body>
</html>
'''

#add the coordinates from the Instagram API
index = contents.find("var locations =") + 15
newContents = contents[:index] + coordinates + contents[index:]

#open browser with content data from the api
def main():
    browseLocal(newContents)


def toFile(text, filename):
    #Write a file with the given name and the given text.
    output = open(filename,"w")
    output.write(text)
    output.close()

#safe tge un
def browseLocal(webpageText, filename='map.html'):
    toFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))


main()