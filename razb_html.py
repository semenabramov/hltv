#it fckg good
from turtle import st
from bs4 import BeautifulSoup
import db
import os

l = [x[1] for x in os.walk('html/teams')]
# print(l[0])

tmp = os.listdir("html/teams/astralis")

def get_arr(str):
    tmp = ""
    for c in stats_row:
        # c.find("span")
        tmp += c.find_all("span")[1].text
        tmp+='|'
        # print(tmp.text)

    itmp = []
    sttmp = ""
    for ch in tmp:
        if ch !='/' and ch !='|' and ch !=' ' and ch !='%':
            sttmp+=ch
            continue
        if ch == "|" or ch == "/":
            itmp.append(sttmp)
            sttmp = ""    
    return itmp



db = db.DataBase("data.bd")

for name in l[0]:
    
    maps = os.listdir(f"html/teams/{name}")
    
    for m in maps:
        print(f"---{m[:-5].upper()}---")
        with open(f"html/teams/{name}/{m}", encoding="utf-8") as file:
            src = file.read()
            soup = BeautifulSoup(src, "html.parser")
            stats_row = soup.find_all(class_ = "stats-row")
            stat = get_arr(stats_row)
            db.add_stat(m[:-5],name,stat)
            
            
            
    


# with open("Ancient.html", encoding="utf-8") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "html.parser")

# stats_row = soup.find_all(class_ = "stats-row")


# tmp = ""
# for c in stats_row:
#     # c.find("span")
#     tmp += c.find_all("span")[1].text
#     tmp+='|'
#     # print(tmp.text)

# itmp = []
# sttmp = ""
# for ch in tmp:
#     if ch !='/' and ch !='|' and ch !=' ' and ch !='%':
#         sttmp+=ch
#         continue
#     if ch == "|" or ch == "/":
#         itmp.append(sttmp)
#         sttmp = ""    

# # print(itmp)

# db = db.DataBase("C:\\work\\python\\parser\\hltv\\data.bd")

# inf = ['times_played','wins','drows','loses','total_rounds','rounds_won','win_persent','pristol_rounds','pistol_rounds_won','pistol_win_persent','ct_win_persent',"t_win_persent"]

# db.add_team("astralis")

# db.add_stat("ancient",1,itmp,inf)

