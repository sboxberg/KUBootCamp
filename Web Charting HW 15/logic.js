// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson"
var faultsUrl = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json"

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(data.features);
});

function createFeatures(earthquakeData) {
  console.log(earthquakeData);
  // Define a function we want to run once for each feature in the features array
  // Give each feature a popup describing the place and time of the earthquake
  function onEachFeature(feature, layer) {
    layer.bindPopup("<h3>" + feature.properties.place +
      "</h3><hr><p>" + "Magnitude: " + feature.properties.mag + ". " + new Date(feature.properties.time) + "</p>");
  }
  function getColor (x){
    return x > 6 ? "#800026" :
            x > 5.5 ? "#BD0026" :
            x > 5 ? "#E31A1C" :
            x > 4.5 ? "#FC4E2A" :
            x > 4 ? "#FD8D3C" :
            x > 3.5 ? "#FEB24C" :
            x > 3 ? "#FED976" :
                  "#FFEDA0";  
  }
  // var legend = L.control({position: 'bottomright'});
  // legend.onAdd = function (myMap) {
  
  //   var div = L.DomUtil.create('div', 'info legend'),
  //       grades = [0, 3, 3.5, 4, 4.5, 5, 5.5, 6],
  //       labels = [];

  //   // loop through our density intervals and generate a label with a colored square for each interval
  //   for (var i = 0; i < grades.length; i++) {
  //       div.innerHTML +=
  //           '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
  //           grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
  //   }

  //   return div;
  // };

  // legend.addTo(myMap);


  // Create a GeoJSON layer containing the features array on the earthquakeData object
  // Run the onEachFeature function once for each piece of data in the array
  var earthquakes = L.geoJSON(earthquakeData, {
    style: function(feature) {
      return {
        color: getColor(feature.properties.mag),
        // fillColor: getColor(feature.properties.mag),
        fillOpacity: 0.8};
    },
    pointToLayer: function(feature, latlng) {
      return new L.CircleMarker(latlng, {radius: feature.properties.mag * 4});
    },
    onEachFeature: onEachFeature
  });

  // Sending our earthquakes layer to the createMap function
  createMap(earthquakes);
}

function createMap(earthquakes) {

  // Define variables for our base layers
  let mapboxUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}';
  let accessToken = 'pk.eyJ1Ijoic2JveGJlcmciLCJhIjoiY2pmeDVrdDl2MDAyNjMzcDJyZDQ2eDV6MiJ9.S0u6RJV8VJijFYOe9D3aRQ';
  let satelliteMap = L.tileLayer(mapboxUrl, {id: 'mapbox.satellite', maxZoom: 20, accessToken: accessToken});
  let outdoorsMap = L.tileLayer(mapboxUrl, {id: 'mapbox.outdoors', maxZoom: 20, accessToken: accessToken});

  // Define a baseMaps object to hold our base layers
  var baseMaps = {
    "Satellite Map": satelliteMap,
    "Outdoors Map": outdoorsMap
  };

  // Create overlay object to hold our overlay layer
  var overlayMaps = {
    Earthquakes: earthquakes,
    // Faults:faults
  };

  // Create our map, giving it the satellitemap and earthquakes layers to display on load
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [satelliteMap, earthquakes]
  });

  // Create a layer control
  // Pass in our baseMaps and overlayMaps
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
}
