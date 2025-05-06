from search import search
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

    textfield = ft.TextField(label="Busca algo")

    things = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        textfield,
                        ft.ElevatedButton("Buscar", on_click=buscar),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        ),
    )

    def route_change(route):
        if page.route == "/detalle":
            from test2 import detalle_view
            page.views.clear()
            page.views.append(detalle_view(page))
            page.update()

    page.on_route_change = route_change
    page.add(things, lista_resultados)

ft.app(main)
