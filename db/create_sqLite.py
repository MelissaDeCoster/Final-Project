import pandas as pd
#sqlite
from sqlalchemy import create_engine
import os
census_data = pd.read_csv("Census_Data.csv")
#create connection
connection_string = "sqlite:///Census_data.sqlite"
engine = create_engine(connection_string)
#Let's clean the headers as we dont like spaces or special characters there.
headers = list(census_data.columns) 
headers = [item.replace(" ", "_") for item in headers]
#remove excape character
headers = [item.replace("+", "greater") for item in headers]
census_data.columns = headers
engine.execute("CREATE TABLE Census_data(ID INTEGER PRIMARY KEY AUTOINCREMENT, Community_Area_Number INT, COMMUNITY_AREA_NAME TEXT, PERCENT_OF_HOUSING_CROWDED INT, PERCENT_HOUSEHOLDS_BELOW_POVERTY INT, PERCENT_AGED_16greater_UNEMPLOYED, PERCENT_AGED_25greater_WITHOUT_HIGH_SCHOOL_DIPLOMA INT, PERCENT_AGED_UNDER_18_OR_OVER_64 INT,PER_CAPITA_INCOME_ INT, HARDSHIP_INDEX INT);")
####### PLUG that data into SQLITE#####
census_data.to_sql(name="Census_data", con=engine, if_exists="append", index=False)
#####SHOW ME some of the Data#####
pd.read_sql_query("SELECT * FROM Census_data",con=engine).head()