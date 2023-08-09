from dotenv import load_dotenv
import os
import requests

load_dotenv('.env')
api_key = os.getenv('API_KEY')

def get_summoner_by_summoner_name(server, summoner_name):
    url = "https://" + server + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    response = requests.get(url)
    return response