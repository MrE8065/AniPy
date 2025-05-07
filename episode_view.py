import flet as ft
import flet_video as fv
from play import get_direct_link

def video_view(page: ft.Page):
    ep_name = page.client_storage.get("ep_name")
    ep_link_raw = page.client_storage.get("ep_link")
    
    ep_link = get_direct_link(ep_link_raw)

    return ft.View(
        "/episodio",
        controls=[
            ft.AppBar(
                title=ft.Text(ep_name),
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: page.go("/detalle"))
            ),
            fv.Video(
                playlist=fv.VideoMedia(ep_link, http_headers={"Referer": "https://yourupload.com"}),
                expand=True,
                aspect_ratio=16 / 9,
                volume=100,
                autoplay=True,
                muted=False
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )