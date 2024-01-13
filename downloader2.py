import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

def download_video():
    url = urlEntry.get()
    resolution = resolution_var.get()

    status_label.pack(pady=(10, 5))
    progress_label.pack(pady=(10, 5))
    progress_bar.pack(pady=(10, 5))

    try:
        yt = YouTube(url, on_progress_callback=on_progess)
        stream = yt.streams.filter(res=resolution, file_extension="mp4", progressive=True).first()

        download_path = os.path.join("Downloads", f"{yt.title}.mp4")
        stream.download(output_path=download_path)
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")

def on_progess(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completed = bytes_downloaded / total_size * 100

    progress_label.configure(text=str(int(percent_completed)) + "%")
    progress_label.update()

    progress_bar.set(float(percent_completed / 100))

# background
root = ctk.CTk() 
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# create window
root.title("YT Downloader")
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

# content frame
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# Label and textbox for URL
url_label = ctk.CTkLabel(content_frame, text="Enter YT url: ")
urlEntry = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(10, 5))
urlEntry.pack(pady=(10, 5))

# download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=(10, 5))

# resolution
resolutions = ["720p", "480p", "360p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, textvariable=resolution_var)
resolution_combobox.pack(pady=(10, 5))
resolution_combobox.set("720p")

# progress bar
progress_label = ctk.CTkLabel(content_frame, text="0%")

# progress label
progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)

# status label
status_label = ctk.CTkLabel(content_frame, text="Download Complete")

# start program
root.mainloop()