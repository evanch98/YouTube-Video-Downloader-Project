from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('600x300')
root.resizable(0, 0)
root.title("YouTube Video Downloader")
Label(root, text = 'YouTube Downloader', font = 'arial 20 bold').pack()

link = StringVar()
Label(root, text = 'Paste Link Here:', font = "arial 15 bold").place(x = 220, y = 100)
link_enter = Entry(root, width = 95, textvariable = link).place(x = 12, y = 130)

def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='Download Complete', font = 'arial 15').place(x = 205, y = 200)

Button(root, text = 'Download', font = 'arial 12 bold', bg = 'light blue', padx = 2, command=downloader).place(x = 250, y = 160)
root.mainloop()
