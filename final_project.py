import requests # this pulls data out of websites
import bs4  #this allows to call the data in differnet ways 
import pandas as pd  # turns link into html  
import matplotlib.pyplot as plt  #plots data

#the url for the world population 
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
#reads the html into pandas 
dfs = pd.read_html(url)
 #finds the correct data frame to take the data to plot from  
df = dfs[1]

#print(df[('Rank', 'Rank')])


#defines df as the data country and population
df = df[[('Country / Dependency', 'Country / Dependency'), ('Population', 'Numbers')]]
#makes the data of populaitons into an integer 
df = df.astype({ ('Population', 'Numbers'):'int'})
#df = df. head(10)
#picks rows 1 to 11
df = df.loc[1:11]

#plots the grpah with the country on the x axis ands populaiton opn the y axis. It also makes the grpah a bar graph
df.plot(x=('Country / Dependency','Country / Dependency'), y= ('Population', 'Numbers'), kind = "bar")
#shows the graph
plt.show()

