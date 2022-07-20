import imp
from time import sleep
import requests
from bs4 import BeautifulSoup
import os
from pars_stat import *

def getTeams(file):
    teams = []
    with open(file,'r') as f:
        while True:
            # считываем строку
            team = f.readline()
            # прерываем цикл, если строка пустая
            if not team:
                break
            # выводим строку

            teams.append(team.strip())
    return(teams)


if __name__ =="__main__":
    teams = getTeams('Data/Teams_BigEvents.txt')
    #print(teams)
    
    browser = create_browser(r'C:\\work\\python\\parser\\chromedriver') #DON'T FORGET TO CHANGE THIS AS YOUR DIR

    for team in teams:
        print(f"----{team.split('/')[1].upper()}----")
        parsMaps(team,browser)