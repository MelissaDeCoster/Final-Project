import os
from flask import Flask, render_template, jsonify, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()



app = Flask(__name__)
    
# ************** Database Setup ***************
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://admin:NUDataScience2019@nu-chicago-crime-app.ccjnkjeza5yv.us-east-2.rds.amazonaws.com:3306/chicago_crime_app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Attach db to Flask app so Flask handels db session managment and other good things
db = SQLAlchemy(app)

data = {}
e = db.get_engine()
table_names = ['graphdata', 'mapdata', 'three_day_forecast', 'scikitlearn_results'] #e.table_names()
for name in table_names:
	tbl = e.execute('SELECT * FROM {}'.format(name)).fetchall()
	data[name] = pd.DataFrame(tbl)

# Futher down in code, to access data:
data['graphdata'] 



# *********************************************
# ************** WEBPAGES *********************
# *********************************************

@app.route("/")
def renderHome():
    return render_template("index.html")

# *********************************************
# ************** API ENDPOINTS ****************
# *********************************************

@app.route("/api/graph/<crime>")
def lStationsJson(crime):
    tbl = data['graphdata']
    results = tbl[tbl[3] == crime]
    json_str = results.to_json(orient="records")
    return Response(response=json_str, status=200, mimetype='application/json')

@app.route("/api/map/<crime>")
def lStationsJson2(crime):
    tbl = data['mapdata']
    results = tbl[tbl[3] == crime]
    json_str = results.to_json(orient="records")
    return Response(response=json_str, status=200, mimetype='application/json')

@app.route("/api/forecast")
def lStationsJson3():
    tbl = data['three_day_forecast']
    json_str = tbl.to_json(orient="records")
    return Response(response=json_str, status=200, mimetype='application/json')

@app.route("/api/prediction/<day>/<crime>")
def lStationsJson4(day, crime):
    tbl = data['scikitlearn_results']
    results = tbl[tbl[1] == day and tbl[7] == crime]
    json_str = tbl.to_json(orient="records")
    return Response(response=json_str, status=200, mimetype='application/json')





    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)