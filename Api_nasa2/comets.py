import requests
import os

def get_commet_data(api_key):
    print("::: COMETS INFORMATION")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
#Main
api_key_nasa = 'c9hkw2qN7iXHdixPD2OKlTMNTNBe0x1qFGxkABFo'
get_commet_data(api_key_nasa) 