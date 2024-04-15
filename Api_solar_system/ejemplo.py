import requests
import json
import os

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
        print("\n#### Planets ####")
        for planet in data["bodies"]:
            if planet["bodyType"]== "Planet":
              print(f"Name: {planet['englishName']}")
              print(f"Gravity: {planet['gravity']}")
              print(f"Inclination: {planet['inclination']}")
              print(f"bodyType: {planet['bodyType']}")
              print("")  
              print("")             
    elif option == "2":
      # Implementar la lógica para obtener y mostrar datos de lunas}
      if data:
        for Moon in data:
          print(f"Nombre: {Moon['name']}")
          print(f"Radio: {Moon['radius']}")
          print(f"Gravedad: {Moon['gravity']}")
          print("----------")
      else:
        print("Error al obtener datos de planetas.")
      data = get_data("https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet", "Moon")
      # ...
    elif option == "3":
      # Implementar la lógica para obtener y mostrar datos de estrellas
      data = get_data("https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet", "star")
      # ...
    elif option == "4":
      # Implementar la lógica para obtener y mostrar datos de asteroides
      data = get_data("https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet", "asteroid")
      # ...
    elif option == "5":
      # Implementar la lógica para obtener y mostrar datos de cometas
      data = get_data("https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet", "comet")
      # ...
    elif option == "6":
      print("Saliendo del programa...")
      break
    else:
      print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
  main()
    
  