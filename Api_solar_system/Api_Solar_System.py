import requests #let 'u get data fromn api-url
import json #Leer  los datos en json
import os #Let 'u execute os commands

def get_data():
    os.system("clear") #Clear scream
    print(":: SOLAR SYSTEM INFORMATION")
    api_url= "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    try: 
      response = requests.get(api_url)
      if response.status_code == 200:
        data = json.loads(response.content)
        filtered_data = [item for item in data if item["bodyType"] == body_type]
        return filtered_data
      else: print(f"Error: {response.status_code}")
      return None
    except Exception as e:
      return None
def main():
  """
  Función principal.
  """
  while True:
    print("### MENÚ PRINCIPAL ###")
    print("[1]. Planetas")
    print("[2]. Lunas")
    print("[3]. Estrellas")
    print("[4]. Asteroides")
    print("[5]. Cometas")
    print("[6]. Salir")

    option = input("::: Elige una opción: ")

    if option == "1":
        api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        response = requests.get(api_url)
        data = response.json()
        print("\n#### PLANETS ####")
        for planet in data["bodies"]:
            if planet["bodyType"]== "Planet":
              print(f"Nombre en ingles: {planet['englishName']}")
              print(f"Gravedad: {planet['gravity']}")
              print(f"Densidad: {planet['density']}")
              print(f"Incinacion: {planet['inclination']}")
              print(f"Es un planeta: {planet['isPlanet']}")
              print(f"Tipo de cuerpo: {planet['bodyType']}")
              print("")  
              print("")             
    elif option == "2":
        api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        response = requests.get(api_url)
        data = response.json()
        print("\n#### MOONS ####")
        for moon in data["bodies"]:
            if moon["bodyType"]== "Moon":
              print(f"Nombre: {moon['englishName']}")
              print(f"Gravedad: {moon['gravity']}")
              print(f"Densidad: {moon['density']}")
              print(f"Incinacion: {moon['inclination']}")
              print(f"Es un planeta: {moon['isPlanet']}")
              print(f"Tipo de cuerpo: {moon['bodyType']}")
              print("")  
              print("")             
    elif option == "3":
        api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        response = requests.get(api_url)
        data = response.json()
        print("\n#### STARS ####")
        for star in data["bodies"]:
            if star["bodyType"]== "Star":
              print(f"Nombre: {star['englishName']}")
              print(f"Gravedad: {star['gravity']}")
              print(f"Densidad: {star['density']}")
              print(f"Incinacion: {star['inclination']}")
              print(f"Es un planeta: {star['isPlanet']}")
              print(f"Tipo de cuerpo: {star['bodyType']}")
              print("")  
              print("")    
    elif option == "4":
        api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        response = requests.get(api_url)
        data = response.json()
        print("\n#### ASTEROIDS ####")
        for asteroid in data["bodies"]:
            if asteroid["bodyType"]== "Asteroid":
              print(f"Nombre: {asteroid['englishName']}")
              print(f"Gravedad: {asteroid['gravity']}")
              print(f"Densidad: {asteroid['density']}")
              print(f"Incinacion: {asteroid['inclination']}")
              print(f"Es un planeta: {asteroid['isPlanet']}")
              print(f"Tipo de cuerpo: {asteroid['bodyType']}")
              print("")  
              print("")   
    elif option == "5":
        api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        response = requests.get(api_url)
        data = response.json()
        print("\n#### COMETS ####")
        for comet in data["bodies"]:
            if comet["bodyType"]== "Comet":
              print(f"Nombre: {comet['englishName']}")
              print(f"Gravedad: {comet['gravity']}")
              print(f"Densidad: {comet['density']}")
              print(f"Incinacion: {comet['inclination']}")
              print(f"Es un planeta: {comet['isPlanet']}")
              print(f"Tipo de cuerpo: {comet['bodyType']}")
              print("")  
              print("")    
    elif option == "6":
      print("Saliendo del programa...")
      break
    else:
      print("Opción inválida. Intenta de nuevo.")
      print("")
      
if __name__ == "__main__":
  main()
    
  