import os
import json

def load_config():
    config_data = open("config.json").read() 
    data = json.loads(config_data)
    if data:
       token = data["token"]
       owner_id = data["owner_id"]
       return token,owner_id
    else:
        print("[*]Error token não definido,verifique se o arquivo de configuração foi definido corretamente")
    

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def install():
    print("[*] install depentencies please wait")
    os.system("pip install httpx python-telegram-bot scraping34==2.0.0")
