from time import sleep
import requests
from bs4 import BeautifulSoup
import os
from random import uniform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_browser(webdriver_path):
    #create a selenium object that mimics the browser
    browser_options = Options()
    #headless tag created an invisible browser
    browser_options.add_argument("--headless")
    browser_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(webdriver_path, chrome_options=browser_options)
    print("Done Creating Browser")
    return browser


#matchType="BigEvents",startDate="2021-07-15",endDate="2022-07-15",




MAPS = {
    "Dust 2":"31",
    "Ancient":"47",
    "Inferno":"33",
    "Mirage":"32",
    "Nuke":"34",
    "Overpass":"40"
}
matchType="BigEvents"
startDate="2021-07-15"
endDate="2022-07-15"

url = "https://www.hltv.org//stats/teams/4608/natus-vincere?startDate=2021-07-15&endDate=2022-07-15&matchType=BigEvents"

def createNewURL(team,map="Dust 2",matchType="BigEvents",startDate="2021-07-15",endDate="2022-07-15"):
    new_url = "https://www.hltv.org//stats/teams/"+f"map/{MAPS[map]}/"+team+f"?startDate={startDate}&endDate={endDate}&matchType={matchType}"
    return new_url

def parsMaps(team, brous):
    for map in MAPS:
        time = uniform(0.7,1.2)
        sleep(time)
        url = createNewURL(team,map)
        print(f"Sleep time: {time}s ---> {url}")
        team_num, team_name = team.split("/") 
        #print(headers.generate())
        

        if not os.path.isdir(f"html/teams/{team_name}"):
            os.mkdir(f"html/teams/{team_name}")

        brous.get(url)

        src =  brous.page_source
        with open(f"html/teams/{team_name}/{map}.html","w",encoding="utf-8") as file:
           file.write(src)    

if __name__ =="__main__":
    #createNewURL(url)
    #parsMaps("4608/natus-vincere")
    print("Done")
