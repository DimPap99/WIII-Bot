import requests
import time
from bs4 import BeautifulSoup

#Functions:
def Get_Games():
    #making a request to get the source code
    games={}
    source = requests.get("http://makemehost.com/games.php").text
    soup = BeautifulSoup(source,'lxml')
    #finding all the <td> tags.tag is a list with those tags
    tag=soup.find_all('div')


    #Getting the makemehost div
    Makemehost_div_tag=soup.find('div',class_='refreshMeMMH')
    #getting all the <td> from Makemehost div
    Makemehost_td=Makemehost_div_tag.find_all('td')


    for i in range(8,len(Makemehost_td),5):

         #We include in the list the elements starting from 8(the games) and we
         #add +1 (for the capacity) if they are not equal with "".The step of
         #the loop is 5 so that we always loop over the games.
        if Makemehost_td[i].text != "":

            #print(Makemehost_td[i].text)
            games[Makemehost_td[i].text]=Makemehost_td[i+1].text


    #Get the games from Enterprise Gaming in the same way
    Enterprise_Gaming_div_tag=soup.find('div',class_='refreshMeENT')
    #make the list of all the td tags
    Enterprise_Gaming_td=Enterprise_Gaming_div_tag.find_all('td')
    for i in range(4,len(Enterprise_Gaming_td),3):
        if Enterprise_Gaming_td[i].text != "" :
            games[Enterprise_Gaming_td[i].text]= Enterprise_Gaming_td[i+1].text
    Partners_div_tag=soup.find('div',class_='refreshMePARTNERS')
    Partner_td=Partners_div_tag.find_all('td')
    if Partner_td[4].text != "":
        games[Enterprise_Gaming_td[i].text]=Enterprise_Gaming_td[i+1].text
    #games=dict(games)
    return games

#Function for the timer
def Timer():
    current_time=time.gmtime()
    current_day = current_time.tm_mday
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min




#--------------------------------------------------------------------------------



print(Get_Games())
#print(soup.prettify())
#print(alltd)
