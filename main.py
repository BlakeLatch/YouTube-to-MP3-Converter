import tkinter
import customtkinter
from pytube import YouTube


#* Download function
def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        audio =  yt_object.streams.get_audio_only()
        title.configure(text=yt_object.title, text_color="white")
        finished_label.configure(text="")
        audio.download()
        finished_label.configure(text="Download Complete")

    except: 
        finished_label.configure(text="YouTube link is invalid", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    int_percentage = str(int(percentage_of_completion))
    progress.configure(text=int_percentage + "%")
    progress.update()

    #* Updating progress bar
    progress_bar.set(float(percentage_of_completion) / 100)


#* System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#* Our app frame
app = customtkinter.CTk()
app.geometry("720x480")

#* Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

#* Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#* Finished Downloading
finished_label = customtkinter.CTkLabel(app, text="")
finished_label.pack()

#* Progress percentage
progress = customtkinter.CTkLabel(app, text="0%");
progress.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)


#* Download Button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

#* Run app
app.mainloop()