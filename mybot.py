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

#Function for the timer returns True when the now_hour and now_minute (which are the time of the user)
#is equal to the specified operation time of the bot else it returns False
def Timer(time_to_operate,current_hour,current_minute):
    operation_hour = current_hour + time_to_operate[0]
    operation_minute = current_minute + time_to_operate[1]

    mytime = time.gmtime()
    now_hour = mytime.tm_hour
    now_minute = mytime.tm_min
    if now_hour == operation_hour and now_minute == operation_minute:
        return True

    return False




#End of Functions--------------------------------------------------------------------------------

current_time = time.gmtime()
current_hour = current_time.tm_hour
current_minute = current_time.tm_min
print(current_hour,current_minute)
hours = int(input("how many hours would you like the bot to operate"))
minutes = int(input("how many minutes would you like the bot to operate"))
time_to_operate=(hours,minutes)
stop=Timer(time_to_operate,current_hour,current_minute)
print(Get_Games())
while not stop:
    print(Get_Games())
    stop=Timer(time_to_operate,current_hour,current_minute)
    time.sleep(180)

#print(soup.prettify())
#print(alltd)
