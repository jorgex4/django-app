import requests #let 'u get data fromn api-url
import os #Let 'u execute os commands

def get_data():
    os.system("clear") #Clear scream
    print(":: SOLAR SYSTEM INFORMATION")
    api_url= "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"

    try:
        #Request to API
        response = requests.get(api_url)
        response.raise_for_status() #If error
        data = response.json()

        print("### MAIN MENU ###")
        print("[1]. Planets")
        print("[2]. Moons")
        print("[3]. Stars")
        print("[4]. Asteoids")
        print("[5]. Comets")
        print("[6]. Exit")

        opt = input("::: Press any option")
       
        return data

    except requests.exceptions.RequestException as e:
        print(f"API error{e}") #=> print(API error",e) 

#Main
info = get_data()
print(info)
