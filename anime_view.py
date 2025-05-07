import flet as ft
from get import get_anime, get_eps

def detalle_view(page: ft.Page):
    anime_link = page.client_storage.get("anime_link")
    titulo, sinopsis, valoracion, imagen_url = get_anime(anime_link)
    episodios = get_eps(anime_link)

    titulo_txt = ft.Text(titulo, weight=ft.FontWeight.BOLD, size=20)
    imagen = ft.Image(imagen_url, border_radius=10)
    desc = ft.Text(sinopsis, size=16)
    val = ft.Text("Valoración: "+valoracion + "⭐", size=16)

    # Crear la ListView con los episodios
    eps = ft.ListView(expand=True, spacing=10)

    for ep_titulo, link in episodios:
        eps.controls.append(
            ft.ListTile(
                title=ft.Text(ep_titulo),
                on_click=lambda e, url=link, name=ep_titulo: ver_ep(e, url, name)
            )
        )
        
    def ver_ep(e, url, name):
        page.client_storage.set("ep_link", url)
        page.client_storage.set("ep_name", name)
        page.go("/episodio")

    return ft.View(
        "/detalle",
        controls=[
            ft.AppBar(title=ft.Text("Detalles del Anime"), leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: page.go("/"))),
            ft.Row(
                controls=[
                    imagen,
                    ft.Column(
                        controls=[titulo_txt, val, desc, eps],
                        expand=True,
                        alignment=ft.MainAxisAlignment.START,
                        spacing=20
                    )
                ],
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=20
            )
        ]
    )
