import flet as ft
from search import get_anime

def detalle_view(page: ft.Page):
    anime_link = page.client_storage.get("anime_link")
    titulo, sinopsis, valoracion, imagen = get_anime(anime_link)

    titulo_txt = ft.Text(titulo, weight=ft.FontWeight.BOLD)
    imagen = ft.Image(src=imagen)
    desc = ft.Text(sinopsis)
    val=ft.Text(valoracion+"⭐")
    eps=ft.ListView()

    return ft.View(
        "/detalle",
        controls=[
            ft.Row(
                controls=[
                    imagen,
                    ft.Column(
                        controls=[titulo_txt, val, desc, eps],
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ],
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
    )