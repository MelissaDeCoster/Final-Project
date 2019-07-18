function optionChanged(crimeOption){
    d3.json(`/api/temp_v_incidents/${crimeOption}`).then( (data) => {
        var panel = d3.select("#graph-display");

        console.log('Option selected: ' + crimeOption);
        panel.html("");
        panel.text(data.graph_type);
        console.log('Here\'s the data: ' + data.data);
    })
}

function buildCharts(crimeOption) {
    d3.json(`/samples/${crimeOption}`).then((data) => {
      const otu_ids = data.otu_ids;
      const otu_labels = data.otu_labels;
      const crimeOption_values = crimeOption.sample_values;

    // Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
    var pieData = [
        {
          values: sample_values.slice(0, 10),
          labels: otu_ids.slice(0, 10),
          hovertext: otu_labels.slice(0, 10),
          hoverinfo: "hovertext",
          type: "pie"
        }
      ];
  
      var pieLayout = {
        margin: { t: 0, l: 0 }
      };
  
      Plotly.plot("pie", pieData, pieLayout);
    });
  }
  