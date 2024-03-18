# -*- coding: utf-8 -*-
"""
@author: Brais Lorenzo Fernández
"""
import requests

import random


#Definir funcion de pillar battle.log
#%232UYUR0J2G
token = "" # Insert token for Brawl_stars API

def proc_tag(tag): # Tags need to have %23 to be processed from the API
    tag = tag[1:]
    tag = '%23' + tag
    return tag

def log_battle(tag, key): #Function get battle_log from user.
    headers = {
        'Accept': 'application/json',
        'authorization': 'Bearer {}'.format(key)}
    request_battle_log = requests.get('https://api.brawlstars.com/v1/players/{}/battlelog'.format(tag), headers = headers)
    
    battle = request_battle_log.json() #watch out for utf-8 encoding
    return battle


def battle_time(battle_log,i):
    for i in range(len(battle_log['items'])):
        return battle_log['items'][i]['battleTime']

def get_tag(tag_list):
    size = len(tag_list)
    r_num = random.randint(0,size-1)
    return tag_list[r_num]

def used_tag(tag,usedtags):
    if tag in usedtags:
        return True
    else:
        return False


def show_modes(battle_log): #show the different modes in a battle_log
    for i in range(len(battle_log['items'])):
        print(battle_log['items'][i]['event']['mode'])

def get_mode(battle_log, i): #return the mode of the battle.
    return battle_log["items"][i]['event']['mode']

def get_battletime(battle_log, i):
    return battle_log["items"][i]['battleTime']

def get_duration(battle_log, i):
    return battle_log["items"][i]['battle']['duration']
    
def get_map(battle_log,i):
    return battle_log["items"][i]['event']['map']

def get_stpl(battle_log,i):
    return battle_log["items"][i]['battle']['starPlayer']['tag']

def get_stplbr(battle_log,i):
    return battle_log["items"][i]['battle']['starPlayer']['brawler']['name']

def team_get(battle_log,i,l):
    team = []
    for player in range(len(battle_log['items'][i]['battle']['teams'][l])):
        team.append(battle_log['items'][i]['battle']['teams'][l][player]['tag'])
    return team

def team_trophies(battle_log, i, l):
    team_trophies = {}
    for player in range(len(battle_log['items'][i]['battle']['teams'][l])):
        tag = battle_log['items'][i]['battle']['teams'][l][player]['tag']
        trophy = battle_log['items'][i]['battle']['teams'][l][player]['brawler']['trophies']
        team_trophies.update( {tag : trophy} )
    return team_trophies

def team_brawlers(battle_log, i , l):
    team_brawler = {}
    for player in range(len(battle_log['items'][i]['battle']['teams'][l])):
        tag = battle_log['items'][i]['battle']['teams'][l][player]['tag']
        brawler = battle_log['items'][i]['battle']['teams'][l][player]['brawler']['name']
        team_brawler.update( {tag : brawler} )
    return team_brawler
    

def team_size(battle_log,i,team):
    return battle_log['items'][i]['battle']['teams'][team]
  
def team_tag(battle_log,i,team,size):
    team = []
    for k in range(size):
        tag = battle_log['items'][i]['battle']['teams'][team][k]['tag']
        team.append(tag)
    return team
        
# ============================================================================= NOT NEEDED
# def win_team(battle_log, i, star):
#     size_team = len(battle_log['items'][i]['battle']['teams'][0])
#     team = []
#     team.append(battle_log['items'][i]['battle']['teams'][0])
# =============================================================================

#Functions to retrieve info from players
# EXAMPLE
# =============================================================================
#response = requests.get('https://api.brawlstars.com/v1/players/%232UYUR0J2G', headers=headers)
#res = response.json()   
#res['highestTrophies']
# ============================================================================= 
        
        



