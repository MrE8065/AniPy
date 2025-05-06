import flet as ft

def main(page: ft.Page):
    page.title="AniPy"

    imagen=ft.Image(src="https://www3.animeflv.net/uploads/animes/covers/4173.jpg")
    desc=ft.Text("Lorem ipsum dolor sit amet consectetur adipiscing elit suspendisse fermentum, pellentesque parturient sociosqu litora class lobortis facilisi urna ullamcorper morbi, gravida odio congue enim ut nulla cum eu.\n Curabitur consequat netus lobortis felis himenaeos cubilia semper nisi at tortor, porta dictum donec sagittis nostra parturient risus dapibus odio per, a elementum integer arcu blandit sodales nibh fringilla mus.\n Condimentum suscipit viverra fermentum parturient libero eros nec et, eget magnis class dis dignissim quis maecenas quam, rhoncus arcu velit fusce donec in ante. Turpis litora ridiculus curabitur ad nibh lacinia proin pellentesque rutrum conubia, nisl praesent accumsan ligula phasellus convallis cubilia cum montes, dictum a scelerisque dictumst vivamus arcu eget at aptent.\n Fusce interdum aliquet curae ligula iaculis nec neque ultrices vel, scelerisque fames semper sed mi commodo natoque est netus, euismod id pharetra congue fermentum pellentesque rhoncus maecenas.\n Curabitur dictumst vel dui in ante mi himenaeos, eu malesuada potenti ligula sem iaculis faucibus semper, sagittis quisque morbi ornare ac mattis.", expand=True)

    page.add(
        ft.Container(
            content=(
                ft.Row(
                    controls=[
                            imagen,
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Container(desc, border=ft.border.all(2, ft.Colors.RED)),
                                        ft.Container(
                                            ft.Column(),
                                            border=ft.border.all(2, ft.Colors.BLUE), expand=True
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                border=ft.border.all(2,ft.Colors.GREEN),
                                expand=True,
                                alignment=ft.alignment.center
                            )
                        ]
                )
            ),
            border=ft.border.all(2, ft.Colors.AMBER),
            expand=True
        )
    )

ft.app(main)