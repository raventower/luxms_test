import json
import requests

class APIRequests():
    def __init__ (self):
        self.episode_path='https://rickandmortyapi.com/api/episode/'
        self.character_path='https://rickandmortyapi.com/api/character/'

    def get_episode_json(self, num_episode:str):
        return json.loads(requests.get(self.episode_path+num_episode).content)

    def get_origin_name_of_character(self, character_url:str):
        return json.loads(requests.get(character_url).content)['origin']['name']
    
    def get_character_name(self, character_url:str):
        return json.loads(requests.get(character_url).content)['name']