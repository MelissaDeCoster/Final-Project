
var static_crime = document.getElementById("staticcrime");
var forecast_crime = document.getElementById("forecastcrime");
var predict_crime1 = document.getElementById("predict_crime1");
var predict_crime2 = document.getElementById("predict_crime2");
var predict_crime3 = document.getElementById("predict_crime3");

var options = ["BATTERY", "BURGLARY", "CONCEALED CARRY LICENSE VIOLATION", "CRIM SEXUAL ASSAULT", "CRIMINAL DAMAGE"
,"GAMBLING", "HOMICIDE", "HUMAN TRAFFICKING", "INTERFERENCE WITH PUBLIC OFFICER", "LIQUOR LAW VIOLATION", "MOTOR VEHICLE THEFT"
,"NON-CRIMINAL", "OBSCENITY", "OFFENSE INVOLVING CHILDREN","OTHER NARCOTIC VIOLATION","PROSTITUTION", "PUBLIC INDECENCY", 
"PUBLIC PEACE VIOLATION", "ROBBERY", "SEX OFFENSE","STALKING","THEFT","WEAPONS VIOLATION"];


for (var i = 0; i < options.length; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    static_crime.appendChild(el);
}

for (var i = 0; i < options.length; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    forecast_crime.appendChild(el);
}

