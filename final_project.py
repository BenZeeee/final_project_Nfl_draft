import requests # this pulls data out of websites
import bs4  #this allows to call the data in differnet ways 
import pandas as pd  # turns link into html  
import matplotlib.pyplot as plt  #plots data

# # #puts the link to a variable 
# url = "https://en.wikipedia.org/wiki/Greece"
# response = requests.get(url)
# soup = bs4.BeautifulSoup(response.text)

# pretty_html_string = soup.prettify()

# with open("greece_wiki.htm", "w") as f:
#     f.write(pretty_html_string)


#df = pd.read_csv("greece_wiki.htm")
#print(df.columns)











url = "https://en.wikipedia.org/wiki/Greece"
dfs = pd.read_html(
    url, 
    match = "Largest cities or towns in Greece"
 
)
#print(dfs)
df = dfs[0]
print(df.info())
df.rename(
    columns={
       "(.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:\"[ \"}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:\" ]\"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}vte Largest cities or towns in Greece Hellenic Statistical Authority 2011 census[310], Rank.1)]":"rank"


    })
print(df)
# df = df[["Name", "Pop."]].astype("int")
# print(df)
# df.plot(x="Name", y= "Pop.")
# plt.show()
