import tkinter as tk
import vlc
import os

def start_player(video_url):
    root = tk.Tk()
    root.title("Reproductor VLC")
    root.configure(bg="black")
    is_paused = False
    is_fullscreen = False

    # Verificar si el enlace contiene "vidcache" y agregar el http-referrer
    if "vidcache" in video_url:
        vlc_args = '--http-referrer=https://yourupload.com'
    else:
        vlc_args = ''

    # VLC con Referer si es necesario
    instance = vlc.Instance(vlc_args)
    player = instance.media_player_new()
    media = instance.media_new(video_url)
    player.set_media(media)

    # Marco para video
    video_frame = tk.Frame(root, bg="black", width=800, height=450)
    video_frame.pack(fill="both", expand=True)

    # Pantalla de ayuda inicial
    help_frame = tk.Frame(root, bg="black")
    help_frame.place(relx=0.5, rely=0.5, anchor="center")

    help_text = (
        "Controles del reproductor:\n\n"
        "⏯  Espacio: Pausar / Reproducir\n"
        "⏪  Flecha izquierda: Retroceder 10s\n"
        "⏩  Flecha derecha: Avanzar 10s\n"
        "🖥   F: Pantalla completa\n"
        "ℹ   H: Mostrar ayuda\n"
        "⎋  Escape: Salir de pantalla completa"
    )

    label_help = tk.Label(help_frame, text=help_text, fg="white", bg="black", font=("Helvetica", 12), justify="left")
    label_help.pack(pady=10)

    btn_start = tk.Button(
        help_frame,
        text="Adelante ▶",
        command=lambda: start_video(),
        bg="#1c1c1c",
        fg="white",
        activebackground="#333",
        activeforeground="white",
        relief=tk.FLAT,
        font=("Helvetica", 11, "bold"),
        padx=10,
        pady=5
    )
    btn_start.pack(pady=10)

    # Enlazar VLC a frame
    root.update_idletasks()
    if os.name == "nt":
        player.set_hwnd(video_frame.winfo_id())
    else:
        player.set_xwindow(video_frame.winfo_id())

    def start_video():
        help_frame.destroy()  # Cierra el menú de ayuda
        player.play()

    def show_help_again(event=None):
        # Pausar solo si el video no está pausado
        if not is_paused:
            toggle_pause()  # Pausar el video
        # Re-crear el frame de ayuda
        help_frame = tk.Frame(root, bg="black")
        help_frame.place(relx=0.5, rely=0.5, anchor="center")

        label_help = tk.Label(
            help_frame,
            text=(
                "Controles del reproductor:\n\n"
                "⏯️  Espacio: Pausar / Reproducir\n"
                "⏪  Flecha izquierda: Retroceder 10s\n"
                "⏩  Flecha derecha: Avanzar 10s\n"
                "🖥️   F: Pantalla completa\n"
                "ℹ️   H: Mostrar ayuda\n"
                "⛔  Escape: Salir de pantalla completa"
            ),
            fg="white", bg="black", font=("Helvetica", 12), justify="left"
        )
        label_help.pack(pady=10)

        btn_start = tk.Button(
            help_frame,
            text="Continuar ▶",
            command=start_video,
            bg="#1c1c1c",
            fg="white",
            activebackground="#333",
            activeforeground="white",
            relief=tk.FLAT,
            font=("Helvetica", 11, "bold"),
            padx=10,
            pady=5
        )
        btn_start.pack(pady=10)

    def toggle_pause():
        nonlocal is_paused
        if is_paused:
            player.play()  # Reanudar la reproducción
        else:
            player.pause()  # Pausar el video
        is_paused = not is_paused

    def rewind():
        current_time = player.get_time()
        player.set_time(max(current_time - 10000, 0))

    def forward():
        current_time = player.get_time()
        duration = player.get_length()
        player.set_time(min(current_time + 10000, duration))

    def toggle_fullscreen():
        nonlocal is_fullscreen
        is_fullscreen = not is_fullscreen
        root.attributes("-fullscreen", is_fullscreen)

    def exit_fullscreen(event=None):
        if is_fullscreen:
            toggle_fullscreen()

    # Teclas
    def handle_space(event):
        toggle_pause()

    def handle_left(event):
        rewind()

    def handle_right(event):
        forward()

    def handle_f(event):
        toggle_fullscreen()

    root.bind("<space>", handle_space)
    root.bind("<Left>", handle_left)
    root.bind("<Right>", handle_right)
    root.bind("<f>", handle_f)
    root.bind("<Escape>", exit_fullscreen)
    root.bind("<h>", show_help_again)

    root.geometry("900x540")
    #root.focus_force() # Asegura que la ventana esté en primer plano
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

if __name__=="__main__":
    # Llamada a la función con el enlace de video
    VIDEO_URL = "https://vidcache.net:8161/a20250408v4CsyCF15IR/video.mp4"
    start_player(VIDEO_URL)
