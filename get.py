import requests
from bs4 import BeautifulSoup

# Código para extraer los títulos y enlaces de anime de la lista HTML
def search(something):
    
    base_url="https://www3.animeflv.net/browse?q="
    response = requests.get(base_url+something)
    
    if response.status_code == 200:
        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar todos los artículos de anime
        anime_articles = soup.find_all('article', class_='Anime')
        
        # Lista para almacenar los resultados (título, enlace)
        anime_info = []
        
        for article in anime_articles:
            # Encontrar el enlace principal del anime
            link_element = article.find('a')
            if link_element:
                # Extraer la URL
                link = link_element.get('href')
                # Extraer la carátula
                image= link_element.find('img')['src']
                # Extraer el título (está en h3)
                title_element = link_element.find('h3', class_='Title')
                if title_element:
                    title = title_element.text.strip()
                    # Añadir la información a la lista
                    anime_info.append((title, image, link))
        return anime_info
    else:
        return f"Error al cargar la página: {response.status_code}"
    
def get_anime(anime_link):
    response = requests.get("https://www3.animeflv.net"+anime_link)
    if response.status_code==200:
        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Obtiene el título del episodio
        titulo=soup.find('h1', class_='Title').text.strip()
        # Obtiene la sinopsis del episodio
        sinopsis=soup.find('div', class_='Description').text.strip()
        # Obtiene la valoración del episodio
        valoracion=soup.find('span', class_='vtprmd').text.strip()
        # Obtiene la carátula del episodio
        imagen="https://www3.animeflv.net"+soup.find('div', class_='Image').find('img')['src']
        
        return titulo, sinopsis, valoracion, imagen
    else:
        return f"Error al cargar la página: {response.status_code}"
    
def get_eps(anime_link):
    response=requests.get("https://www3.animeflv.net"+anime_link)
    
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
                
        # Si encontramos la variable "episodes" en los scripts
        if episodes_data:
            # Procesar manualmente la cadena de episodios
            episodes_data = episodes_data.strip('[]').split('],[')
                
            for ep_data in episodes_data:
                ep_parts = ep_data.strip('[]').split(',')
                if len(ep_parts) >= 1:
                    episode_number = ep_parts[0].strip()
                    # Crear la URL del episodio
                    episode_url = f"https://www3.animeflv.net/ver/{anime_link.split('/')[-1]}-{episode_number}"
                    # Añadir la información a la lista
                    episode_title=f"Episodio {episode_number}"
                    anime_eps.append((episode_title, episode_url))
                    
            # Ordenar por número de episodio (convertido a entero)
            anime_eps = sorted(anime_eps, key=lambda x: int(x[0].split()[1]))
            return anime_eps
        
    else:
        return f"Error al cargar la página: {response.status_code}"

if __name__=="__main__":
    
    hola="a"
    #print(search(hola))
    
    print(get_eps("/anime/lazarus"))