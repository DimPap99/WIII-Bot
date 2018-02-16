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


for i in range(8,len(Makemehost_td),5):

     #We include in the list the elements starting from 8(the games) and we add +1 (for the capacity) if they are not blank.The step of the loop is 5 so that we always loop over the games.
    if Makemehost_td[i].text!="":

        print(Makemehost_td[i].text)
        games.append((Makemehost_td[i].text,Makemehost_td[i+1].text))
print(games)
#print(soup.prettify())
#print(alltd)
