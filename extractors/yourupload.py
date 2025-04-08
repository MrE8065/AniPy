import requests
import re

def get_direct_url(url):
    response = requests.get(url)

    # Buscar el campo 'file' dentro del objeto jwplayerOptions
    match = re.search(r"jwplayerOptions\s*=\s*{.*?file:\s*['\"]([^'\"]+\.mp4)['\"]", response.text, re.DOTALL)
    if match:
        return match.group(1)
    return None

if __name__ == "__main__":
    result = get_direct_url("https://www.yourupload.com/embed/e7Cf6FMCS163")
    print(result)
