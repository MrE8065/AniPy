import requests
from bs4 import BeautifulSoup
import os
from play import play_episode

def get_desc(anime):
    real_url="https://www3.animeflv.net"+anime
    response=requests.get(real_url)
    
    if response.status_code == 200:
        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar la descripción del anime
        desc = soup.find('div', class_='Description')
        anime_desc = desc.p.text.strip()
        return anime_desc
    
    else:
        return f"Error al cargar la página: {response.status_code}"

def get_eps(anime):
    real_url="https://www3.animeflv.net"+anime
    response=requests.get(real_url)
    
    if response.status_code == 200:
        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscar todos los scripts para encontrar la variable episodes
        scripts = soup.find_all('script')
        episodes_data = None
        
        # Lista para almacenar los resultados
        anime_eps = []
        
        # Extraer la información de episodios del script
        for script in scripts:
            if script.string and 'var episodes = ' in script.string:
                # Encontramos el script que contiene los episodios
                script_content = script.string
                start_index = script_content.find('var episodes = ') + len('var episodes = ')
                end_index = script_content.find('];', start_index) + 1
                if start_index > 0 and end_index > start_index:
                    episodes_data = script_content[start_index:end_index]
                    break
                
        # Si encontramos la variable episodes en los scripts
        if episodes_data:
            # Procesar manualmente la cadena de episodios
            episodes_data = episodes_data.strip('[]').split('],[')
                
            for ep_data in episodes_data:
                ep_parts = ep_data.strip('[]').split(',')
                if len(ep_parts) >= 1:
                    episode_number = ep_parts[0].strip()
                    # Crear la URL del episodio
                    episode_url = f"https://www3.animeflv.net/ver/{anime.split('/')[-1]}-{episode_number}"
                    # Añadir la información a la lista
                    episode_title=f"Episodio {episode_number}"
                    anime_eps.append((episode_title, episode_url))
                    
            # Ordenar por número de episodio (convertido a entero)
            anime_eps = sorted(anime_eps, key=lambda x: int(x[0].split()[1]))
            return anime_eps
        
    else:
        return f"Error al cargar la página: {response.status_code}"

def handle_anime(anime, title):
    print("Sinopsis")
    print("-" * 40)
    print(get_desc(anime))
    print("-" * 40)
    print("Episodios:")
    print("-" * 40)
    resultados = get_eps(anime)

    # Verificar si hay resultados y son del tipo esperado (lista)
    if resultados and isinstance(resultados, list):
        # Mostrar solo los títulos, enumerados
        for i, (episode_title, _) in enumerate(resultados, 1):
            print(f"{i}. {episode_title}")
        print("-" * 40)
        
        # Mostrar cantidad de resultados
        print(f"\nSe encontraron {len(resultados)} episodios para '{title}'")
        
        # Seleccionar un episodio para reproducirlo
        if len(resultados) > 0:
            try:
                seleccion = int(input("\n¿Qué episodio quieres ver? (Ingresa el número o 0 para salir): "))
                if 1 <= seleccion <= len(resultados):
                    titulo_seleccionado, enlace_seleccionado = resultados[seleccion-1]
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Has seleccionado: {titulo_seleccionado}\n")
                    print("Reproducir episodio")
                    print("Enlace del episodio: "+enlace_seleccionado)
                    play_episode(enlace_seleccionado)
                    # Aquí podrías agregar código para reproducir/descargar el anime
                elif seleccion == 0:
                    print("¡Hasta pronto!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor ingresa un número válido.")
    elif isinstance(resultados, str) and "Error" in resultados:
        print(resultados)  # Muestra el mensaje de error
    else:
        print("No se encontraron resultados para tu búsqueda.")

if __name__=="__main__":
    
    hola="/anime/a-channel"
    print(get_desc(hola))
    print("------------------------------------")
    print(get_eps(hola))