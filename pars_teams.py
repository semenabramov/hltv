import requests
from bs4 import BeautifulSoup


def read_html(name):
    with open(name,"r",encoding="utf-8") as file:
        src = file.read()
    return src 


def parsTeams(matchType="BigEvents",startDate="2021-07-15",endDate="2022-07-15"): #https://www.hltv.org/stats/teams?startDate=2021-07-15&endDate=2022-07-15&matchType=BigEvents
    url = f"https://www.hltv.org/stats/teams?startDate={startDate}&endDate={endDate}&matchType={matchType}"
    headers ={
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    src = req.text
    with open(f"html/Teams_{matchType}.html","w",encoding="utf-8") as file:
       file.write(src)


def createTeamsFile(Teams="Teams_BigEvents"):
    src = read_html(f"html/{Teams}.html")
    soup = BeautifulSoup(src, "html.parser")
    teams = []

    all_title = (soup.findAll(class_='teamCol-teams-overview'))[1:]


    for title in all_title:
        team_url = title.find('a')
        #print(team_url['href'])
        #print(title.text)
        teams.append(team_url['href'])

    with open(f"Data/{Teams}.txt","w") as file:
        for team in teams:
            index = team.find("teams/") + 6
            team_name = team[index:].split('?')[0]
            print(team_name)
            file.write(team_name+"\n")
    
    with open(f"Data/{Teams}_URL.txt","w") as file:
        for team in teams:
            file.write("https://www.hltv.org/"+team+"\n")


if __name__ == "__main__":
    createTeamsFile()
    print('Done')