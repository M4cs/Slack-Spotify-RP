import requests
import json
import os
import time
from ssrp.utils.colors import *

class API:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.parse_config()
        self.current_spotify_token = self.config['spotify_auth_token']
        self.refresh_token = self.config['spotify_refresh_token']
        self.slack_workspace_tokens = self.config['slack_workspaces']
        self.update_interval = self.config['update_interval']
        self.format = self.config['format']
        
    def parse_config(self):
        with open(self.config_file, 'r+') as jc:
            config = json.load(jc)
        return config
    
    def check_token(self):
        if not self.test_spotify_token():
            if not self.test_spotify_token():
                error("Couldn't re-authenticate with Spotify! Please delete your config and go through setup again!")
                exit()
            else:
                return True
        return True
    
    def unset_status(self):
        for workspace in self.slack_workspace_tokens:
            requests.post("https://slack.com/api/users.profile.set", data=json.dumps({
                    "profile": {
                    "status_text": "",
                    "status_emoji": "",
                    "status_expiration": 0
                }}), headers={"Content-Type": "application/json; charset=utf-8", "Authorization": "Bearer " + workspace})
    
    def get_current_playing_song(self):
        if self.check_token():
            headers = {"Authorization": "Bearer " + self.current_spotify_token}
            url = "https://api.spotify.com/v1/me/player/currently-playing"
            res = requests.get(url, headers=headers)
            if res.status_code != 200:
                return (None, None, None, False)
            album_name = None
            artist = None
            name = None
            resobj = res.json()
            if resobj.get('item'):
                playing = False
                if resobj.get('is_playing'):
                    playing = resobj.get('is_playing')
                if resobj['item'].get('album'):
                    album_name = resobj['item']['album']['name']
                if resobj['item'].get('artists'):
                    artist = resobj['item']['artists'][0]['name']
                if resobj['item'].get('name'):
                    name = resobj['item']['name']
                return (name, artist, album_name, playing)
            else:
                return (None, None, None, False)
        else:
            return (None, None, None, False)
            
    def set_now_playing(self):
        song, artist, album, playing = self.get_current_playing_song()
        for workspace in self.slack_workspace_tokens:
            if not playing:
                show_music("Not Playing Anything")
                requests.post("https://slack.com/api/users.profile.set", data=json.dumps({
                    "profile": {
                    "status_text": "Spotify: Not Playing Anything",
                    "status_emoji": ":musical_note:",
                    "status_expiration": 0
                }}), headers={"Content-Type": "application/json; charset=utf-8", "Authorization": "Bearer " + workspace})
            else:
                status = self.format.replace("artist", artist).replace("song", song).replace("album", album)
                show_music("Now Playing: " + status)
                requests.post("https://slack.com/api/users.profile.set", data=json.dumps({
                    "profile": {
                    "status_text": "Spotify: " + status,
                    "status_emoji": ":musical_note:",
                    "status_expiration": 30
                }}), headers={"Content-Type": "application/json; charset=utf-8", "Authorization": "Bearer " + workspace})
            time.sleep(2)
    
            
    def test_spotify_token(self):
        headers = {"Authorization": "Bearer " + self.current_spotify_token}
        url = "https://api.spotify.com/v1/me"
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            self.refresh_access_token()
            return False
        else:
            return True
        
    def refresh_access_token(self):
        res = requests.get("https://ssrp.maxbridgland.com/getRefreshForSpotify/" + self.refresh_token)
        if res.status_code == 200:
            resobj = res.json()
            if resobj.get("access_token"):
                self.current_spotify_token = resobj['access_token']
                with open(self.config_file, "w+") as jf:
                    confObj = json.load(jf)
                    confObj['spotify_auth_token'] = resobj['access_token']
                    if resobj.get('refresh_token'):
                        self.refresh_token = resobj['refresh_token']
                        confObj['spotify_refresh_token'] = resobj['refresh_token']
                    json.dump(confObj, jf, indent=4)
            else:
                error("Couldn't re-authenticate with Spotify! Please delete your config and go through setup again!")
                exit()