// Creating map object
var index;
var layer1;
var map2 = L.map("map2", {
  center: [41.8321135, -87.6804194],
  zoom: 10
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
}).addTo(map2);



d3.select("#staticcrime").on("change", function () {
  crime = d3.select("#staticcrime").node().value;
 
  buildCharts(crime);
  buildMap(crime);
});


function buildMap(crime) {
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var mapURL = "/api/map/" + crime;
  // @TODO: Build a Bubble Chart using the sample data
  d3.json(mapURL, function (error, response) {

    var crimecount = response.map(function (x) {
      return x["1"];
    });

    var community = response.map(function (x) {
      return x["2"];
    });

    var crimetally = []
    crimecount.forEach((count) => {
      crimetally.push(parseInt(count));
    });

    //Create binning end points for various colors
    var maxvalue = Math.max.apply(null, crimetally);
    var midvalue = Math.round(maxvalue / 2);
    var quartervalue = Math.round(midvalue / 2);
    var topquartervalue = Math.round(midvalue + quartervalue);
    var minvalue = Math.min.apply(null, crimetally);

    console.log(crime + "Max: "+maxvalue);
    console.log(crime + "Top Quarter:" +topquartervalue);
    console.log("Mid:" +midvalue);
    console.log("Bottom Quarter: "+quartervalue);
    console.log("Min: "+minvalue);



    var link = "https://nu-chicago-crime-app.s3.us-east-2.amazonaws.com/Boundaries+-+Community+Areas+(current).geojson";


    function chooseColor(feature) {
      var thiscurrentarea = feature.properties.community
      index = community.findIndex(community => community === feature.properties.community.split(' ')
            .map(w => w[0].toUpperCase() + w.substr(1).toLowerCase())
            .join(' '));
      if (crimetally[index] <= maxvalue & crimetally[index] > topquartervalue) {
        color = "rgb(122, 0, 45)";
      } else if (crimetally[index] <= topquartervalue & crimetally[index] > midvalue) {
        color = "rgb(169, 62, 60)";
      } else if (crimetally[index] <= midvalue & crimetally[index] > quartervalue) {
        color = "rgb(207, 112, 71)";
      } else if (crimetally[index] <= quartervalue & crimetally[index] > minvalue) {
        color = "rgb(232, 155, 83)";
      } else {
        color = "rgb(243, 191, 94)";
      }
      return color;
    }


    // Grabbing our GeoJSON data..
    d3.json(link, function (data) {
      // Creating a geoJSON layer with the retrieved data
      console.log(layer1);
      if (layer1 == null){
        // Do nothing
      }else{
        map2.removeLayer(layer1);
      }
      layer1 = L.geoJson(data, {
        // Style each feature (in this case a neighborhood)
        style: function (feature) {
          return {
            color: "black",
            // Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
            fillColor: chooseColor(feature),
            fillOpacity: 1,
            weight: 1.5
          };
        },

        // Called on each feature
        onEachFeature: function (feature, layer) {
          // Set mouse events to change map styling
          layer.on({
            // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
            mouseover: function (event) {
              layer = event.target;
              layer.setStyle({
                fillOpacity: 0.5
              });
            },
            // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
            mouseout: function (event) {
              layer = event.target;
              layer.setStyle({
                fillOpacity: 1
              });
            },
          });


          // index = community.findIndex(community => community === feature.properties.community.split(' ')
          //   .map(w => w[0].toUpperCase() + w.substr(1).toLowerCase())
          //   .join(' '));
          // console.log(crimetally[index]); // 3

          // Giving each feature a pop-up with information pertinent to it
          layer.bindPopup("<h3>" + feature.properties.community + "</h3> <hr> <h4>" + crime +" "+ crimetally[index] + "</h4>");



        }
      }).addTo(map2);
    });


  });
};

d3.select("#staticcrime").dispatch("change");



