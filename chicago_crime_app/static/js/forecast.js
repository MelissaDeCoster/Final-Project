/*<i class="fas fa-sun fa-5x"></i> /*sunshine*/
/*<i class="fas fa-cloud-showers-heavy fa-5x"></i> /*rain*/
/*<i class="fas fa-cloud-sun fa-5x"></i> /*partial cloud*/
/*<i class="fas fa-cloud"></i> /*full cloud*/
/*<i class="far fa-snowflake"></i> /*snow flake*/

// @TODO: Use `d3.json` to fetch the sample data for the plots
var forecastURL = "/api/forecast";
// @TODO: Build a Bubble Chart using the sample data
d3.json(forecastURL, function (error, response) {

    // creating desc object for icons
    var weather_dict = {
        'Sunny' : "fas fa-sun fa-5x",     
        'Scattered Thunderstorms': "fas fa-cloud-showers-heavy fa-5x",
        'Thunderstorms': "fas fa-cloud-showers-heavy fa-5x",
        'Mostly Sunny': "fas fa-cloud-sun fa-5x",
        'Isolated Thunderstorms': "fas fa-cloud",
        'Partly Cloudy': "fas fa-cloud-sun fa-5x",
        'Snow': "far fa-snowflake",
        'Clear': "fas fa-cloud"

        
    }

    //Map the Json to Variables for Day and Date
    var date = response.map(function (x) {
        return x["1"];
    });

    var day = response.map(function (x) {
        return x["2"];
    });

    var desc = response.map(function (x) {
        return x["3"];
    });

    //Change the Date placeholders to 
    document.getElementById("dayonedate").textContent = day[0] + " "+ date[0];
    document.getElementById("daytwodate").textContent = day[1] + " " + date[1];
    document.getElementById("daythreedate").textContent = day[2] + " "+date[2];

    // Creating desc icon and connecting to index.html
    document.getElementById("dayonecloud").className = weather_dict[desc[0]];
    document.getElementById("daytwocloud").className = weather_dict[desc[1]];
    document.getElementById("daythreecloud").className = weather_dict[desc[2]];


    var temp = response.map(function (x) {
        return x["6"];
    });

    document.getElementById("dayonetemp").textContent = temp[0].replace(",", "/") + "º F";
    document.getElementById("daytwotemp").textContent = temp[1].replace(",", "/") + "º F";
    document.getElementById("daythreetemp").textContent = temp[2].replace(",", "/") + "º F";

});





