from flask import Flask, render_template
import summoner_v4
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<server>/<name>')
def profile(server, name):
    profile_data = summoner_v4.get_summoner_by_summoner_name(server, name)
    profile_data_json = json.loads(profile_data.text)
    return render_template('profile.html', profile_data=profile_data_json)

if __name__ == '__main__':
    app.run(debug=True)