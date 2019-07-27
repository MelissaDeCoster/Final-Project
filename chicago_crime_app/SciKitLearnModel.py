#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Dependencies

#Numpy
import numpy as np
# Pandas
import pandas as pd

#datetime
import datetime

# SQL Alchemy
from sqlalchemy import create_engine

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()


#scikit-learn
from sklearn import linear_model
from sklearn.metrics import log_loss
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import statsmodels.api as sm

#webscraping
import requests
from bs4 import BeautifulSoup


# In[5]:


#Create connection to AWS backend database

engine = create_engine("mysql://admin:NUDataScience2019@nu-chicago-crime-app.ccjnkjeza5yv.us-east-2.rds.amazonaws.com:3306/chicago_crime_app")
conn = engine.connect()


# In[6]:


#Query the database to gather the training data and store it in a pandas Datafrane

train_data = pd.read_sql("SELECT * FROM grouped_data WHERE Date >= '2010-01-01' AND Date <= '2013-01-01';", conn)


# In[7]:


#Convert the Date into a DateTime objoect

train_data['Date'] = pd.to_datetime(train_data['Date'])


# In[8]:


#Create a list of fields to use as the predictors (independent varaible)

predictors =  train_data[['Temp_Avg_F', 'Community_Area_Number']]
le_primary_type = train_data['Primary_Type']

#Since Primary Type is a string, we will use a Label Encoding tool to assign each possible type a numeric value

le = preprocessing.LabelEncoder()
le.fit(le_primary_type)
le.classes_
le_primary_type_transformed = le.transform(le_primary_type)
le_primary_type_transformed

#Update the training data with the encoded labels
predictors['Primary_Type'] = le_primary_type_transformed


#We can use this predictions_test to make sure we can decode the encoded labels

predictions_test = le.inverse_transform(le_primary_type_transformed)


# In[12]:


#Set the dependent variable as the count of incidents

target = train_data[['incident_count']]


# In[13]:


# Since we're doing a linear regression, and the community area number and primary type label are ordinal data
# We can use a technique called OneHotEncoding to make sure the model treats each possibility equally, and doesn't weight them
# Inaccuratly based on the magnitude of the numeric value


primary_type_ohe = OneHotEncoder()
community_area_ohe = OneHotEncoder()
X = primary_type_ohe.fit_transform(predictors.Primary_Type.values.reshape(-1,1)).toarray()
Xm = community_area_ohe.fit_transform(predictors.Community_Area_Number.values.reshape(-1,1)).toarray()


# In[14]:


#Here we will update the training data with the Primary type one hot encoded

dfOneHot = pd.DataFrame(X, columns = ["Primary_Type_"+str(int(i)) for i in range(X.shape[1])])
predictors.reset_index(drop=True, inplace=True)
dfOneHot.reset_index(drop=True, inplace=True)
predictors = pd.concat([predictors, dfOneHot], axis=1)


# In[15]:


#Here we will update the training data with the Community Area Number one hot encoded

dfOneHot = pd.DataFrame(Xm, columns = ["Community_Area_Number_"+str(int(i)) for i in range(Xm.shape[1])])
predictors = pd.concat([predictors, dfOneHot], axis=1)


# In[16]:


#Set the X and Y axes for the regression to predictors and target defined above, respectively

x = predictors
y = target


# In[17]:


#Create the model and look at the OLS Regression Results

model = sm.OLS(target.astype(float),x.astype(float)).fit()
predictions = model.predict(x)
model.summary()


# In[18]:


#Perform the Linear Regression and fit the model

lm = linear_model.LinearRegression()
model = lm.fit(x,target)


# In[19]:


#Run the predictions and check the score

predictions = lm.predict(x)

lm.score(x,target)


# In[20]:


#Scrape Chicago Weather from Weather.com


page=requests.get("https://weather.com/weather/tenday/l/bb3a65580eeeed24af39f5db9d1f57695d4b0767bf2fe3c5745e803ee36ed41b")
content=page.content
soup=BeautifulSoup(content,"html.parser")
l=[]
all=soup.find("div",{"class":"locations-title ten-day-page-title"}).find("h1").text
 

table=soup.find_all("table",{"class":"twc-table"})
for items in table:
	for i in range(len(items.find_all("tr"))-1):
		d = {}
		try:
			d["day"]=items.find_all("span",{"class":"date-time"})[i].text
			d["date"]=items.find_all("span",{"class":"day-detail"})[i].text			
			d["desc"]=items.find_all("td",{"class":"description"})[i].text
			d["temp"]=items.find_all("td",{"class":"temp"})[i].text
			d["precip"]=items.find_all("td",{"class":"precip"})[i].text
			d["wind"]=items.find_all("td",{"class":"wind"})[i].text
			d["humidity"]=items.find_all("td",{"class":"humidity"})[i].text
		except:
			d["day"]="None"
			d["date"]="None"
			d["desc"]="None"
			d["temp"]="None"
			d["precip"]="None"
			d["wind"]="None"
			d["humidity"]="None"
		#print("")
		l.append(d)

weather_df = pd.DataFrame(l)
print(weather_df)


# In[21]:


#Grab the next 3 days worth of weather data

next_three_days_df = weather_df.iloc[1:4]


# In[22]:


#Do a little cleanup

next_three_days_df["temp"]= next_three_days_df["temp"].str.replace('°', ',')

next_three_days_df["temp"] = next_three_days_df["temp"].map(lambda x: str(x)[:-1])
next_three_days_df[['high','low']] = next_three_days_df.temp.str.split(",",expand=True)
next_three_days_df


# In[23]:


#Push the table to the database

engine = create_engine("mysql://admin:NUDataScience2019@nu-chicago-crime-app.ccjnkjeza5yv.us-east-2.rds.amazonaws.com:3306/chicago_crime_app")
conn = engine.connect()

next_three_days_df.to_sql(con=engine, name='three_day_forecast', if_exists='replace')


# In[24]:


#31 primary types, 77 comunity areas ---- Create lists for looping / creating predictions

Temp_Avg_F_list = list(next_three_days_df['high'])
Community_Area_Number_list = list(range(1, 78))
Primary_Type_list = list(range(1, 34))
Day_list = list(range(1,4))
print(Temp_Avg_F_list)
print(Community_Area_Number_list)
print(Primary_Type_list)
print(Day_list)


# In[28]:


#Set the test values for a new prediction

Community_Area_Number = 45
Temp_Avg_F = 82
Primary_Type = 1


# In[29]:


#Define the predict function


def predict(Temp_Avg_F, Community_Area_Number, Primary_Type):
    tomorrow_df_starter = predictors.iloc[[0]]
    for col in tomorrow_df_starter.columns:
        tomorrow_df_starter[col].values[:] = 0


    tomorrow_df_starter['Temp_Avg_F'] = Temp_Avg_F
    Community_Area_Column_Name = 'Community_Area_Number_' + str((Community_Area_Number -1))
    Primary_Type_Column_Name = 'Primary_Type_' + str((Primary_Type-1))
    tomorrow_df_starter[Community_Area_Column_Name]=1
    tomorrow_df_starter[Primary_Type_Column_Name]=1

    tomorrow_df_starter.reset_index(drop=True, inplace=True)
    tomorrow_crime = lm.predict(tomorrow_df_starter)

    return tomorrow_crime


# In[30]:


#Test the function
result = predict(Temp_Avg_F, Community_Area_Number, Primary_Type)
print(result)


# In[31]:


#Set up a results Dataframe to store the results

results_columns = ['Day','Temp_Avg_F','Community_Area_Number', 'Primary_Type', 'Predicted_Incident_Count']

results_df = pd.DataFrame(columns=results_columns)

results_df.head()


# In[23]:


# Nested Loop through all of the possible scenarios

for i in range(0,3):
    Temp_Avg_F = Temp_Avg_F_list[i]
    Day = Day_list[i] 
    
    for j in range(0,77):
        Community_Area_Number = Community_Area_Number_list[j]
        
        for pt in range(0,31):
            Primary_Type = Primary_Type_list[pt]
            

            
            
            try:
                result = predict(Temp_Avg_F, Community_Area_Number, Primary_Type)
                #print(result)
                results_df = results_df.append({'Day': Day, 'Temp_Avg_F': Temp_Avg_F,                                                'Community_Area_Number': Community_Area_Number,                                                'Primary_Type' : Primary_Type,                                                 'Predicted_Incident_Count' : str(result)}, ignore_index=True)
            except:
                print("An exception occurred")
                print(Day)
                print(Temp_Avg_F)
                print(Community_Area_Number)
                print(Primary_Type)
        


# In[24]:


#Make the prediction and display the number of incidents

#tomorrow_crime = lm.predict(tomorrow_df_starter)
#print(tomorrow_crime)
results_df.head(20)


# In[30]:


results_df2 = results_df
results_df2['Predicted_Incident_Count'] = results_df2['Predicted_Incident_Count'].str.replace('[', '')
results_df2['Predicted_Incident_Count'] = results_df2['Predicted_Incident_Count'].str.replace(']', '')
results_df2.head(20)


# In[31]:


# Create Engine and Pass in MySQL Connection
engine = create_engine("mysql://admin:NUDataScience2019@nu-chicago-crime-app.ccjnkjeza5yv.us-east-2.rds.amazonaws.com:3306/chicago_crime_app")
conn = engine.connect()


# In[32]:


#Send Results to AWS
results_df2.to_sql(con=engine, name='scikitlearn_results', if_exists='replace')


# In[ ]:




