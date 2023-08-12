from flask import Flask, render_template, request, redirect
import api
import json

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Search':
                name = request.form['summonerName']
                url = '/profile' + 'euw1' + name
                return redirect(url)
    servers = get_servers()
    return render_template('index.html', servers=servers)


@app.route('/profile/<server>/<name>')
def profile(server, name):
    profile_data_json = get_profile_data_json(server, name)
    
    top_3_champion_names = get_top_3_champion_names(server, profile_data_json['id'])
    top_3_champion_score = get_top_3_champion_score(server, profile_data_json['id'])

    return render_template('profile.html', profile_data=profile_data_json, name=name, top_3_champion_names=top_3_champion_names, top_3_champion_score=top_3_champion_score)


def get_servers():
    with open ('constants/servers.txt') as file:
        servers = file.readlines()
    return servers


def get_champion_name_by_id(id):
    all_champion_data = api.get_all_champion_data()
    all_champion_data_json = json.loads(all_champion_data.text)
    for champion_name in all_champion_data_json['data']:
        if int(all_champion_data_json['data'][champion_name]['key']) == int(id):
            return champion_name
        

def get_top_3_champion_names(server, id):
    all_champion_mastery = api.get_all_champion_mastery(server, id)
    all_champion_mastery_json = json.loads(all_champion_mastery.text)
    top_3_champion_names = []
    top_3_champion_names.append(get_champion_name_by_id(all_champion_mastery_json[0:3][0]['championId']))
    top_3_champion_names.append(get_champion_name_by_id(all_champion_mastery_json[0:3][1]['championId']))
    top_3_champion_names.append(get_champion_name_by_id(all_champion_mastery_json[0:3][2]['championId']))
    return top_3_champion_names


def get_top_3_champion_score(server, id):
    all_champion_mastery = api.get_all_champion_mastery(server, id)
    all_champion_mastery_json = json.loads(all_champion_mastery.text)
    top_3_champion_score = []
    top_3_champion_score.append(all_champion_mastery_json[0:3][0]['championPoints'])
    top_3_champion_score.append(all_champion_mastery_json[0:3][1]['championPoints'])
    top_3_champion_score.append(all_champion_mastery_json[0:3][2]['championPoints'])
    return top_3_champion_score


def get_profile_data_json(server, name):
    profile_data = api.get_summoner_by_summoner_name(server, name)
    profile_data_json = json.loads(profile_data.text)
    return profile_data_json

if __name__ == '__main__':
    app.run(debug=True)