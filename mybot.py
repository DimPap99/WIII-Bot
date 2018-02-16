import requests
from bs4 import BeautifulSoup

#making a request to get the source code
games=[]
source = requests.get("http://makemehost.com/games.php").text
soup = BeautifulSoup(source,'lxml')
#finding all the <td> tags.tag is a list with those tags
tag=soup.find_all('div')


#Getting the makemehost div
Makemehost_div_tag=soup.find('div',class_='refreshMeMMH')
#getting all the <td> from Makemehost div
Makemehost_td=Makemehost_div_tag.find_all('td')


for i in range(0,len(Makemehost_td)):
     #excluding the elemnts of the list that we do not need and keeping only the games and the capacity of the game's room.
     if Makemehost_td[i].text!="" and "MakeMeHost" not in Makemehost_td[i].text and "Europe" not in Makemehost_td[i].text and "USA" not in Makemehost_td[i].text:
                                        print(Makemehost_td[i].text)
#print(soup.prettify())
#print(alltd)
