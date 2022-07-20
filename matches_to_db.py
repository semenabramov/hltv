from turtle import st
from bs4 import BeautifulSoup
import db
import os

def getMatchs(file_):
    with open(file_,encoding="utf-8") as file:
        matches = []
        src = file.read()
        soup = BeautifulSoup(src, "html.parser")
        results_sublist = soup.find_all(class_ = "results-sublist")
        for date in results_sublist: #по датам
            date_ = date.find(class_="standard-headline").text
            #print(date_)
            for result in date.find_all(class_="result-con"):
                matche_url = "https://www.hltv.org"+result.find('a')['href']
                teams = [x.text for x in result.find_all(class_="team")]
                score = [x.text for x in result.find(class_="result-score").find_all('span')]
                match = [teams[0],teams[1],int(score[0]),int(score[1]),date_,matche_url]
                matches.append(match)
        
        return matches



if __name__ == "__main__":
    
    db = db.DataBase("data.bd")
    file = 'html/Matches_startDate=2021-07-15_endDate=2022-07-15_stars=3.html'
    #db.get_matches()
    matches = getMatchs(file)

    #print(matches)
    for match in matches:
        db.add_matche(match)


