


d3.select("#staticcrime").on("change", function(){
  crime = d3.select("#staticcrime").node().value;
  buildCharts(crime);
});

function buildCharts(crime) {
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var chartsURL = "/api/graph/" + crime;
    // @TODO: Build a Bubble Chart using the sample data
    d3.json(chartsURL, function(error, response) {

      var crimecount = response.map(function(x) {
        return x["1"];
      });

      var temperature = response.map(function(x) {
        return x["2"];
      });

      console.log(response)
       

      var trace1 = {
        type: "scatter",
        mode: "lines",
        x: temperature,
        y: crimecount,
        line: {
          color: "rgb(158, 18, 8)"
        }
      };

      var data = [trace1];

      var layout = {
        title: `${crime} VS TEMPERATURE`,
        xaxis: {
          title: 'TEMPERATURE (°F)',
        },
        yaxis: {
          title: 'TOTAL INCIDENCES SINCE 2010'
        }
      };
      
      Plotly.newPlot("plot", data, layout);

  });
};

d3.select("#staticcrime").dispatch("change");



