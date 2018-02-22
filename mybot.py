import requests
import time
from bs4 import BeautifulSoup
import pygame

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

#Time prints the games whenever the counter is equal to the publish time the user specified
#or whenever counter mod the time the user specified is equal to zero
def Timer(time_limit,counter):

    if time_limit==counter or counter % time_limit == 0:
        Bot_sound()
        print(Get_Games())
    return True
#Specifys the time for the bot to publish
def Publish_Time():
    while True:
        try:
            hours=int(input("Every how many hours do you want the bot to publish the maps? "))
            minutes=int(input("Every how many minutes do you want the bot to publish the maps? "))
            seconds=int(input("Every how many seconds do you want the bot to publish the maps? "))
            break
        except (ValueError):
            print("You didnt give a valid value!")
    total_time_in_seconds= hours * 3600 + minutes * 60 + seconds
    return total_time_in_seconds
def Bot_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("bot_sound.wav")
    pygame.mixer.music.play()

#End of Functions--------------------------------------------------------------------------------

current_time = time.gmtime()
current_hour = current_time.tm_hour
current_minute = current_time.tm_min
current_seconds = 3600 * current_hour + 60 * current_minute
while True:
    try:
        hours = int(input("how many hours would you like the bot to operate "))
        minutes = int(input("how many minutes would you like the bot to operate "))

        break
    except (ValueError):
        print("You didnt give a valid value!")

time_to_operate = hours * 3600 + 60 * minutes
print(time_to_operate)
#time which decides when the bot will publish
time_limit=Publish_Time()


for counter in range(1,time_to_operate +1):
        Timer(time_limit,counter)
        time.sleep(1)


#print(soup.prettify())
#print(alltd)
