import os
from flask import Flask, render_template, jsonify, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd


app = Flask(__name__)
    
# ************** Database Setup ***************

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///PUTDATABASENAMEHERE.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Attach db to Flask app so Flask handels db session managment and other good things
db = SQLAlchemy(app)
# db.engine

path_for_this_file = os.path.dirname(__file__)

# Load in your map csv data
db_table_name = "mapdata"
absolute_csv_path = os.path.join(path_for_this_file,"static","sourcedata","map_data.csv")
df = pd.read_csv(absolute_csv_path)

# Load in graph csv data
db_table_name2 = "graphdata"
absolute_csv_path2 = os.path.join(path_for_this_file,"static","sourcedata","graph_data.csv")
df2 = pd.read_csv(absolute_csv_path2)


print("\nClean and transform ....\n")
# CLEAN
# TRANSFORM
print(df.head())
print(df2.head())

df.to_sql(db_table_name, con=db.engine, if_exists="replace", chunksize=20000)
print("Map Data Loaded!")
df2.to_sql(db_table_name2, con=db.engine, if_exists="replace", chunksize=20000)
print("Graph Data Loaded!")



# *********************************************
# ************** WEBPAGES *********************
# *********************************************

@app.route("/")
def renderHome():
    return render_template("index.html")

# *********************************************
# ************** API ENDPOINTS ****************
# *********************************************

@app.route("/api/cities")
def lStationsJson():
    df = pd.read_sql(f"""
        select  * 
        from    {db_table_name}
        """, db.engine)
    json_str = df.to_json(orient="records")
    return Response(response=json_str, status=200, mimetype='application/json')


@app.route("/api/games")
def lStationsJson2():
    df2 = pd.read_sql(f"""
        select  * 
        from    {db_table_name2}
        """, db.engine)
    json_str = df2.to_json(orient="records")
    return Response(response=json_str, status=200, mimetype='application/json')

@app.route("/api/summary")
def lStationsJson3():
    df3 = pd.read_sql(f"""
        select  * 
        from    {db_table_name3}
        """, db.engine)
    json_str = df3.to_json(orient="records")
    return Response(response=json_str, status=200, mimetype='application/json')



# if __name__ == "__main__":
#     app.run(debug=True)