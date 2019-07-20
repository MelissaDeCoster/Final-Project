import os
from flask import Flask, render_template, jsonify, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import pandas as pd



app = Flask(__name__)
    
# ************** Database Setup ***************
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///static/db/simpledata.sqlite"

# Attach db to Flask app so Flask handels db session managment and other good things
db = SQLAlchemy(app)

data = {}
e = db.get_engine()
table_names = e.table_names()
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


# @app.route("/api/graph")
# def lStationsJson2():
#     graph = pd.read_sql(f"""
#         select  * 
#         from    {graph_data}
#         """, db.engine)
#     json_str = df.to_json(orient="records")
#     return Response(response=json_str, status=200, mimetype='application/json')


    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)