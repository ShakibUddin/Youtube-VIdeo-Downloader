import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from pytube import YouTube

#Frame

root=tk.Tk()
root.configure(background="red")

root.title("Youtube Video Downloader")#Frame title
root.geometry("350x500")#Tkinter window size


#function

def getVidInfo():
    global EntryURL
    string=EntryURL.get()
    yt=YouTube(str(string))

    error=False
    #Checking Checkbox values
    if(AudioButtonVariable.get()==0 and VideoButtonVariable.get()==0):
        tk.messagebox.showerror(title="Warning",message="Please select a format from checkbox")
        error=True
    if ProjectDirectory.get()==0 and EntryLocation.get()=="":
        tk.messagebox.showerror(title="Warning", message="Please provide a directory")
        error=True
    if ProjectDirectory.get()==1 and EntryLocation.get()!="":
        tk.messagebox.showerror(title="Warning", message="Please choose one directory")
        error = True
    if(error==False):
        # checking the details of that video
        tk.messagebox.showinfo(title="Details", message=f" Video Title = {yt.title}.\n Video length = {int(yt.length / 60)} minutes, {yt.length % 60} seconds.\n Video Views = {yt.views}.")

        # checking which file type to downlaod
        if (AudioButtonVariable.get() == 1 and VideoButtonVariable.get() == 0):  # Audio checkbox is on..
            stream = yt.streams.last()
            if ProjectDirectory.get()==1:
                stream.download()  # download just audio
            else:
                stream.download(str(EntryLocation.get())+"/")  # download just audio
            tk.messagebox.showinfo(title="Done !!!",message="Your Audio is downloaded")

        elif (VideoButtonVariable.get() == 1 and AudioButtonVariable.get() == 0):  # video checkbox is on..
            stream = yt.streams.first()
            if ProjectDirectory.get()==1:
                stream.download()
            else:
                stream.download(str(EntryLocation.get())+"/")  # downlaod just video
            tk.messagebox.showinfo(title="Done !!!", message="Your Video is downloaded")

        else:  # both audio video checkbox is on
            stream = yt.streams.last()  # downlaod audio
            if ProjectDirectory.get()==1:
                stream.download()
            else:
                stream.download(str(EntryLocation.get())+"/")


            stream = yt.streams.first()  # download video
            if ProjectDirectory.get() == 1:
                stream.download()
            else:
                stream.download(str(EntryLocation.get()) + "/")

            if ProjectDirectory.get()==1:
                tk.messagebox.showinfo(title="Done !!!", message="File downloaded in project directory")
            else:
                tk.messagebox.showinfo(title="Download Complete",message=f"File downloaded in {EntryLocation.get()}")


fontStyle = tkFont.Font(family="Lucida Grande", size=15)
TextViewURL=tk.Label(root,text="Url :",bg="red",fg="white",font=fontStyle,anchor="center",width=10,pady=10)
TextViewURL.grid(row=0,column=2,pady=20)#TextView

EntryURL=tk.Entry(root,width=40)
EntryURL.grid(row=1,column=2,padx=60)

AudioButtonVariable=tk.IntVar()#Storing Checkbuttons value in this variable..which will return 1 if checked and 0 if unchecked
VideoButtonVariable=tk.IntVar()

Audio=tk.Checkbutton(root,text="Audio",variable=AudioButtonVariable).grid(row=2,column=2,padx=60,pady=10)
Video=tk.Checkbutton(root,text="Video",variable=VideoButtonVariable).grid(row=3,column=2,padx=60,pady=10)


DonwloadLocation=tk.Label(root,text="Download Directory :",bg="red",fg="white",font=fontStyle,anchor="center",width=20,padx=60,pady=10)
DonwloadLocation.grid(row=4,column=2,pady=20)#TextView

EntryLocation=tk.Entry(root,width=40)
EntryLocation.grid(row=5,column=2,padx=60)

ProjectDirectory=tk.IntVar()
Directory=tk.Checkbutton(root,text="Default Project Directory",variable=ProjectDirectory).grid(row=6,column=2,pady=10)

SubmitButton=tk.Button(root,text="Download",width=10,command=getVidInfo).grid(row=7,column=2,pady=10)

root.mainloop()