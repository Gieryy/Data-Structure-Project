import requests
import json
from dotenv import load_dotenv
import os
from datetime import datetime

def load_config():
    load_dotenv()
    config_path = os.getenv("CONFIG_FILE")
    if not config_path:
        raise ValueError("CONFIG_FILE tidak ditemukan.")
    
    with open(rf"{config_path}", 'r') as f:
        file = f.read()
        return json.loads(file)

def create_url(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    return f"{base_url}q={city_name}&appid={api_key}"


def get_weather_data(url):
    response = requests.get(url)
    return response.json()


def convert_to_json(output_file_weather:str, data:dict ,save_to_json=True):
    # weather = []

    if save_to_json:
        with open(output_file_weather, "w") as f:
            json.dump(data, f, indent=4)
        print("Weather data has been saved to weather.json")
    else:
        print("Failed to save weather data")

def main(city_name:list):
    try:
        config_data = load_config()
        api_key = config_data["api_key"]
        
        for i in city_name:
            url = create_url(i, api_key)
            print(f"Fetching data from: {url}") 
            data = get_weather_data(url)
            convert_to_json(f"output_file_weather/{i}.json",data, save_to_json=True)        
            
    except Exception as e:
        raise

if __name__ == "__main__":
    city_name = ["Bandung", "Jakarta", "Surabaya"]
    main(city_name)