import requests
from bs4 import BeautifulSoup
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

import pandas
df = pandas.DataFrame(l)
print(df)
df.to_csv("Weather10DayForecast.csv")	
