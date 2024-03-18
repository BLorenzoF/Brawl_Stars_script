# -*- coding: utf-8 -*-
"""
@author: Brais Lorenzo 
"""

import requests

import json
import pandas as pd
pd.set_option("display.max_columns", 15)
pd.set_option("display.max_rows", 4)
tags = ["#GLQ0L02J","#9PUR9PCCU" ] #User inserts the tag they want if they want to insert a specific tag.

used_tags = []
data = []
counter = 0
for s in tags:
    print('counterA is:',counter)
    counter += 1
    print('counterB is:',counter)
    if counter == 15000:
        print("counter has reached limit: ",counter)
        break
    print(s)
    
    if s in used_tags:
        print('used')
        continue
    else:
        cl_tag = proc_tag(s)
        b_log = log_battle(cl_tag, token) #I retrieve b_log from brawlstars
        print(cl_tag)
        
        try:
            for n in range(len(b_log['items'])):
                print('n es: ',n)            
                mode = get_mode(b_log, n)
                level = get_map(b_log, n)
                battle_time = get_battletime(b_log, n)
            
            
                if mode == 'brawlBall' or mode == 'bounty' or mode == 'heist' or mode == 'gemGrab' or mode == 'siege':
                    print('mode es: ', mode)
                    star = get_stpl(b_log, n) #Star_player_tag
                    star_br = get_stplbr(b_log,n) #Star_player Brawler
                    duration = get_duration(b_log, n)
                    team_winner = []
                    team_loser = []
                    for l in range(len(b_log['items'][n]['battle']['teams'])): #tag_winner,tag_loser
                        team = team_get(b_log,n,l)
                        if star in team:
                            team_winner = team
                        else:
                            team_loser = team
                    all_tags_team = team_winner + team_loser #getting all tags together
                    for thing in all_tags_team:
                        tags.append(thing)
                    trophies_winner = []
                    trophies_loser = []
                
                    for l in range(len(b_log['items'][n]['battle']['teams'])): #trophy W/L
                        team_trophy = team_trophies(b_log,n,l)
                        if star in team_trophy.keys():
                            trophies_winner = list(team_trophy.values())
                        else:
                            trophies_loser = list(team_trophy.values())
                    brawler_winner = []
                    brawler_loser = []
                    for l in range(len(b_log['items'][n]['battle']['teams'])): #brawler W/L
                        team_brawler = team_brawlers(b_log,n,l)
                        if star in team_brawler.keys():
                            brawler_winner = list(team_brawler.values())
                        else:
                            brawler_loser = list(team_brawler.values())
                
                        
                    row = [battle_time, mode, level,duration, star_br, star, team_winner, team_loser, trophies_winner, trophies_loser, brawler_winner, brawler_loser]
                    data.append(row) #### THIS IS WHERE THE DATA IS APPENDED TO
                else:
                    continue
        except:
            pass
    used_tags.append(s) ##To prevent the script from getting into a cycle reusing tags, we append the tag to a reused list.
    print("counter is ",counter)

# A pandas DF is created with the rows to a destination file.
data_l = data.copy()

dt_frame = pd.DataFrame(data = data_l, columns = ["id","game mode","level","game duration","star character","star_tag","team winner","team loser","trophies winner","trophies loser","characters winner","characters loser"])


dt_frame.to_csv("") #Insert destination address

len(used_tags)

import os
os.getcwd()
file1 = open("myfile.txt","w") 
file1.write(used_tags)

with open('listfile.txt', 'w') as filehandle:
    for listitem in used_tags:
        filehandle.write('%s\n' % listitem)










