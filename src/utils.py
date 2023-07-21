import os
import yaml

from datetime import datetime, timedelta

with open("config.yaml", "r") as file:
    CONFIG = yaml.safe_load(file)

def get_today_date():

    today_date = datetime.now()
    today_date_string = today_date.strftime("%Y-%m-%d")

    return today_date_string


def find_pickle_file(today_date, selection):
    model_directory = CONFIG['model_path']
    model_path = os.path.join(model_directory, f"{today_date}_{selection}.pkl")
    print(model_path)
    
    if os.path.exists(model_path):
        return model_path

    yesterday = datetime.strptime(today_date, "%Y-%m-%d") - timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y-%m-%d")
    yesterday_model_path = os.path.join(model_directory, f"{yesterday_date}_{selection}.pkl")
    
    if os.path.exists(yesterday_model_path):
        return yesterday_model_path

