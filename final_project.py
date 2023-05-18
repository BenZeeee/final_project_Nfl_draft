import pandas as pd #This import pulls the data from the links and allows it to be graphed.  
import matplotlib.pyplot as plt #This import graphs the data. 

#This is the link from where the information comes from  
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
#This function reads the html link and makes it usable for pandas so data can be taken.  
dfs = pd.read_html(url)
#This defines the data frame as the correct data from which I need source the information from.  
df = dfs[1]

#This defines the Data I want to pull as the Country and Population.  
df = df[[('Country / Dependency', 'Country / Dependency'), ('Population', 'Numbers')]]
#This turns the data of the "Populaitons" into an integer which allows it to be on the y-axis. 
df = df.astype({ ('Population', 'Numbers'):'int'})
#This selects rows 1 to 11 of the data.
df = df.loc[1:11]

#This plots the data of the "Country" on the x=axis and the "Populaiton" on the y-axis.
#It also makes the grpah a bar graph.
df.plot(x=('Country / Dependency','Country / Dependency'), y= ('Population', 'Numbers'), kind = "bar")
#This shows the graph once it is complete. 
plt.show()

