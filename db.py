from itertools import tee
import sqlite3

class DataBase:
    
    boolact = False
    
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        
        
        
    def add_team(self, team_name):
        with self.connection:
            result = self.cursor.execute("SELECT id FROM teams WHERE team = ?", (team_name,)).fetchmany(1)
            
            if (len(result)==0):
                return self.cursor.execute("INSERT INTO 'teams' ('team') VALUES (?)", (team_name,))       
            else:
                return
        
    def add_stat(self, map, name , stat):
        with self.connection:
            
            result = self.cursor.execute(f"SELECT wins FROM {map.lower().replace(' ','_')} WHERE team = ('{name}')").fetchmany(1)
            
            
            if (len(result) == 0):
                print("---> Add")
                self.cursor.execute(f"INSERT INTO {map.lower().replace(' ','_')} VALUES ( '{name}' { ',' + str(stat).strip('[]')} ) ")
            

    def add_matche(self, data):
        with self.connection:

            #print(f"INSERT INTO matches (team_1,team_2,score_1,score_2,date,url) VALUES ({str(data).strip('[]')})")
            self.cursor.execute(f"INSERT INTO matches (team_1,team_2,score_1,score_2,date,url) VALUES ({str(data).strip('[]')})")

    def get_matches(self):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM matches").fetchall()
            return result

            
    
    #self.cursor.execute("UPDATE all_users SET active = ? WHERE user_id = ?", (active,user_id,))