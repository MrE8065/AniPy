import os
import time
from search import search
from anime import handle_anime

os.system('cls' if os.name == 'nt' else 'clear')

print("""
*-----------------------------------*
|                                   |
|                                   |
|       ¡Bienvenid@ a AniPy!        |
|                                   |
|                                   |
*-----------------------------------*
""")
anime = input("Escribe el anime que quieres ver: ")
print(f"Buscando {anime}...")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
resultados = search(anime)

# Verificar si hay resultados y son del tipo esperado (lista)
if resultados and isinstance(resultados, list):
    print("Resultados encontrados:")
    print("-" * 40)
    # Mostrar solo los títulos, enumerados
    for i, (titulo, _) in enumerate(resultados, 1):
        print(f"{i}. {titulo}")
    print("-" * 40)
    
    # Opcional: Mostrar cantidad de resultados
    print(f"\nSe encontraron {len(resultados)} resultados para '{anime}'")
    
    # Opcional: Permitir seleccionar un anime para ver más detalles
    if len(resultados) > 0:
        try:
            seleccion = int(input("\n¿Qué anime quieres ver? (Ingresa el número o 0 para salir): "))
            if 1 <= seleccion <= len(resultados):
                titulo_seleccionado, enlace_seleccionado = resultados[seleccion-1]
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Has seleccionado: {titulo_seleccionado}\n")
                handle_anime(enlace_seleccionado,titulo_seleccionado)
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