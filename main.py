from get import search
import flet as ft

def main(page: ft.Page):
    page.title = "AniPy"
    lista_resultados = ft.GridView(max_extent=250, child_aspect_ratio=0.67, spacing=10, run_spacing=10, expand=True)

    def ver_anime(e):
        page.client_storage.set("anime_link", e.control.data)
        page.go("/detalle")

    def buscar(e):
        lista_resultados.controls.clear()
        resultados = search(textfield.value)

        if not resultados:
            lista_resultados.controls.append(
                ft.Text("No hay resultados", size=20, weight="bold", text_align=ft.TextAlign.CENTER)
            )
        else:
            for titulo, imagen, url in resultados:
                results_card = ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(src=imagen, width=150, height=250),
                                ft.Text(titulo, weight="bold", width=170, overflow=ft.TextOverflow.ELLIPSIS, text_align=ft.TextAlign.CENTER, max_lines=3)
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        padding=5,
                        on_click=ver_anime,
                        data=url
                    ),
                    elevation=2
                )
                lista_resultados.controls.append(results_card)
        page.update()

    textfield = ft.TextField(label="Busca algo", on_submit=buscar)

    things = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[textfield, ft.ElevatedButton("Buscar", on_click=buscar)],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        ),
        padding=10
    )

    def route_change(route):
        page.views.clear()
        if page.route == "/detalle":
            from anime_view import detalle_view
            page.views.append(detalle_view(page))
        elif page.route == "/episodio":
            from episode_view import video_view
            page.views.append(video_view(page))
        else:
            page.views.append(
                ft.View(
                    "/",
                    controls=[things, lista_resultados],
                    scroll=ft.ScrollMode.AUTO
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")

ft.app(main)
