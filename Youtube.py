from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        locationError.config(text=Folder_Name, fg="blue")

    else:
        locationError.config(text="Choose Folder", fg ="red")

def DownloadVideo():
    choice = YTDChoose.get
    url = ytdEntry.get()

    if(len(url) >1):
        YTDError.config(text="")
        yt = YouTube(url)

        if (choice == choices [0]):
            select = yt.streams.filter(progressive=True).first()

        elif (choice == choices [1]):
            select = yt.streams.filter(progressive=True, file_extension="mp4").last()

        elif (choice == choices [2]):
            select = yt.streams.filter(only_audio=True).first()

    select.download(Folder_Name)
    YTDError.config(text="Download Finished")


#gui for Downloader
root=Tk()
root.title("YouTube Downloader")
root.geometry("450x400")
root.columnconfigure(0, weight=1)

#Label
YTDLabel = Label(root, text="URL of the Video", font=("jost", 16))
YTDLabel.grid()

#entry
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid()

#error message
YTDError = Label(root, text="Error", fg="red", font=("jost", 12))
YTDError.grid()

#save file
saveLabel = Label(root, text="Save Video", font=("jost", 16))
saveLabel.grid()

#save entry
saveEntry = Button(root, width=16, bg="pink", fg="black", text="Choose", command=openLocation)
saveEntry.grid()

#error msg location
locationError = Label(root, text="Error", fg="red", font=("jost", 16))
locationError.grid()

#Quality location
YTDQuality = Label(root, text="Choose Quality", font=("jost", 16))
YTDQuality.grid()

#Quality choose
choices = ["720p", "144p", "Only Audio"]
YTDChoose = ttk.Combobox(root, values=choices)
YTDChoose.grid()

#download
downloadbtn = Button(root, text="Download", width= 12, fg="black", command=DownloadVideo)
downloadbtn.grid()

root.mainloop()