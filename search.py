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
                # Extraer el título (está en h3)
                title_element = link_element.find('h3', class_='Title')
                if title_element:
                    title = title_element.text.strip()
                    # Añadir la información a la lista
                    anime_info.append((title, link))
        return anime_info
    else:
        return f"Error al cargar la página: {response.status_code}"
    
    
if __name__=="__main__":
    
    hola="a"
    print(search(hola))