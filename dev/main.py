import os
import argparse
import json

config_file = "config.json"

def load_config():
    config_data = open(config_file).read() 
    data = json.loads(config_data)

    token = data["token"]
    owner_id = data["owner_id"]
    return token,owner_id
    

def build_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--install",action="store_true")
    parser.add_argument("--token",type=str)
    return parser.parse_args()


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def install():
    print("[*] install depentencies please wait")
    os.system("pip install httpx python-telegram-bot python dotenv rich")
