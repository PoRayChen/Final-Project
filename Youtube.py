from tkinter import *
from pytube import YouTube
from PIL import ImageTk, Image

#GUI
root = Tk()
root.geometry('500x250')
root.resizable(0, 0)
root.title("Video downloader")
Label(root, text='Youtube Video Downloader', font='Vivaldi 16 ').pack()

#function that download it
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='Vivaldi 18').place(x=180, y=210)
    Button(root, text='DOWNLOAD', font='Vivaldi 18', bg='red', padx=2, command=Downloader).place(x=180, y=150)
    #entry
link = StringVar()
Label(root, text='Paste Link Here:', font='Vivaldi 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


root.mainloop()