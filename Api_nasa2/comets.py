import requests 
import os #=> para ehjecutar comandos del sismeta operativo

def get_commet_data(api_key):
    print("::: COMMET INFORMATIONS")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        data = response.json()

        os.system('clear')
        #Show:
        #Comet name
        name = data.get('name', 'Desconocido')
        diameter_km_min = data.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_min', 'Desconocido')
        diameter_km_max = data.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_max', 'Desconocido')
        diameter_ft_min = data.get('estimated_diameter', {}).get('feet', {}).get('estimated_diameter_min', 'Desconocido')
        diameter_ft_max = data.get('estimated_diameter', {}).get('feet', {}).get('estimated_diameter_max', 'Desconocido')
        print("Nombre:", name)
        print("Diámetro estimado (km): Min:", diameter_km_min, "Max:", diameter_km_max)
        print("Diámetro estimado (ft): Min:", diameter_ft_min, "Max:", diameter_ft_max)
        print (f"Orbital data: {data['orbital_data']}")
        

    except requests.exceptions.RequestException as e: 
        print(f"Api error {e}") # => print (API Errro) 
#Main 
api_key_nasa = "fx0IXZKycwcqJ8eA5LVty0zitW9Fcopo53oAVC7T"
get_commet_data(api_key_nasa)