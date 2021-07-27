from os import unlink
import time
import discord
from discord import Color
from discord.ext import commands, tasks
import requests
from requests import api
from requests.api import head
from flask import Flask


my_api_key = "4ad6ab88-7518-4d1a-a3d2-f71947233c6c"

class Faceit:

    game_id = "csgo"
    api_header = {"Authorization":"Bearer " + my_api_key,"content-type": "application/json"}


    def __init__(self,pname) -> None:
        self.pname = pname
       
        

    def get_player_id(self) -> int:
        player_id_request = requests.get(f"https://open.faceit.com/data/v4/players?nickname={self.pname}&game=CSGO",headers=self.api_header)
        player_id_data = player_id_request.json()
        player_id = player_id_data["player_id"]
        return player_id


    def get_player_data(self) -> dict:
        player_data = requests.get(f"https://open.faceit.com/data/v4/players/{self.get_player_id()}",headers=self.api_header)
        player_data_json = player_data.json()
        return player_data_json



    def get_player_stats(self) -> dict:
        player_stats_request = requests.get(f'https://open.faceit.com/data/v4/players/{self.get_player_id()}/stats/{self.game_id}',headers=self.api_header)
        player_stats_json = player_stats_request.json()
        my_player = player_stats_json['lifetime']
        return my_player