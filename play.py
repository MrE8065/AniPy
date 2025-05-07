import requests
import re
import html
import importlib

def get_url(url):
    response = requests.get(url)

    # Buscar la sección de la variable videos
    videos_match = re.search(r'var videos\s*=\s*(\{.*?\});', response.text, re.DOTALL)
    if videos_match:
        videos_str = videos_match.group(1)
        # Decodifica caracteres HTML escapados
        videos_str = html.unescape(videos_str)
        # Quitar barras invertidas en URLs (\/ → /)
        videos_str = videos_str.replace(r'\/', '/')
        # Buscar todos los valores de "url" y "code"
        video_links = re.findall(r'"(?:url|code)"\s*:\s*"([^"]+)"', videos_str)
        return video_links
    else:
        return None  # Si no encuentra ningún enlace

def load_extractor(service_name):
    # Importa el extractor correspondiente
    try:
        # Asumimos que los extractores están en la carpeta 'extractors'
        extractor_module = importlib.import_module(f'extractors.{service_name}')
        return extractor_module.get_direct_url  # Suponemos que cada extractor tiene esta función
    except ModuleNotFoundError:
        return None

def get_direct_link(link):
    # Obtener todos los enlaces de video
    urls = get_url(link)
    if urls:
        # Verificar si alguno de los enlaces contiene un servicio conocido
        for url in urls:
            if "yourupload" in url.lower():
                extractor = load_extractor('yourupload')
            elif "mega" in url.lower():
                extractor = load_extractor('mega')
            else:
                continue  # Si no encontramos un extractor, seguimos con el siguiente enlace
                
            if extractor:
                # Ejecutar el extractor correspondiente
                direct_url = extractor(url)
                if direct_url:
                    return direct_url  # Devolver la URL directa y terminar el flujo de ejecución
    print("No se pudo obtener el enlace directo.")  # Si no se encuentra ningún enlace directo

if __name__ == "__main__":
    get_direct_link("https://www3.animeflv.net/ver/a-channel-1")
