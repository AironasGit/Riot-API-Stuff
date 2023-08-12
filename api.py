from dotenv import load_dotenv
import os
import requests

load_dotenv('.env')
api_key = os.getenv('API_KEY')

def get_summoner_by_summoner_name(server, summoner_name):
    url = "https://" + server + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    response = requests.get(url)
    return response


def get_all_champion_mastery(server, encrypted_summoner_id):
    url = "https://" + server + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + encrypted_summoner_id + "?api_key=" + api_key
    response = requests.get(url)
    return response


def get_all_champion_data():
    url = "http://ddragon.leagueoflegends.com/cdn/13.15.1/data/en_US/champion.json"
    response = requests.get(url)
    return response