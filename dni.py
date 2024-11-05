import requests
from bs4 import BeautifulSoup

def buscar_cuit():
    base_url = "https://www.cuitonline.com/search.php?q="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    while True:
        print("\n----- BUSCAR CUIT Y DNI -----")
        print("by fer")
        print("1. Buscar CUIT")
        print("2. Salir")
        opcion = input("Selecciona una opción (1 o 2): ")

        if opcion == "1":
            query = input("Ingresa un CUIT o término de búsqueda: ")

            response = requests.get(base_url + query, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                search_results = soup.find('div', class_='results', id='searchResults')

                if search_results:
                    hit = search_results.find('div', class_='hit')

                    if hit:
                        nombre = hit.find('h2', class_='denominacion').text.strip()
                        cuil = hit.find('span', class_='cuit').text.strip()
                        print(f"Nombre: {nombre}")
                        print(f"CUIL: {cuil}")
                    else:
                        print(f"No se encontró información específica para el término de búsqueda: {query}")
                else:
                    print("No se encontraron resultados.")
            else:
                print(f"Error en la solicitud: {response.status_code}")

        elif opcion == "2":
            print("Saliendou.")
            break

        else:
            print("invalido")
buscar_cuit()
