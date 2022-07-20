import requests
from bs4 import BeautifulSoup

#https://www.hltv.org/results?startDate=2021-07-19&endDate=2022-07-19&stars=4
#https://www.hltv.org/results?offset=100&startDate=2021-07-19&endDate=2022-07-19&stars=3

def parsMatches(stars="3",startDate="2021-07-19",endDate="2022-07-19"): #https://www.hltv.org/stats/teams?startDate=2021-07-15&endDate=2022-07-15&matchType=BigEvents
    url = f"https://www.hltv.org/results?startDate={startDate}&endDate={endDate}&stars={stars}"
    print(url)
    headers ={
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    src = req.text
    with open(f"html/Matches_startDate={startDate}_endDate={endDate}_stars={stars}.html","w",encoding="utf-8") as file:
        file.write(src)

if __name__ == "__main__":
    parsMatches()