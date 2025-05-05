import flet as ft
from search import search

def main(page: ft.Page):
    
    page.title = "AniPy"
    
    lista_resultados=ft.GridView(max_extent=250, child_aspect_ratio=0.67, spacing=10, run_spacing=10, expand=True)
    
    def algo(e):
        print("Pulsado")
    
    def stuff(e):
        # Limpia la lista de resultados
        lista_resultados.controls.clear()
        # Busca el contenido del textfield
        resultados=search(textfield.value)
        
        for titulo, imagen, url in resultados:
            results_card=ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(src=imagen, width=150, height=250),
                            ft.Text(titulo, weight="bold", width=170, overflow=ft.TextOverflow.ELLIPSIS, text_align=ft.TextAlign.CENTER, max_lines=3)
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=5,
                    on_click=algo
                ),
                elevation=2
            )
            lista_resultados.controls.append(results_card)
        page.update()
    
    textfield=ft.TextField(label="Busca algo")
    
    things = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        textfield,
                        ft.Button("Algo", on_click=stuff),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                
            ]
        ),
    )
    
    page.add(things, lista_resultados)
    
ft.app(main)