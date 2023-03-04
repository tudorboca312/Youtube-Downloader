import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=700, bg="#263D42")
canvas.pack()

def download_video():
    video_url = text_box.get()
    try:
        yt = YouTube(video_url)

        # create firstDownload label
        firstDownload = tk.Label(root, text=f"Video title: {yt.title}", font=("Arial", 10), bg="#263D42", fg="white")
        firstDownload.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        print("Video title:", yt.title)
        stream = yt.streams.get_highest_resolution()

        # remove firstDownload label
        firstDownload.destroy()

        # create secondDownload label
        secondDownload = tk.Label(root, text="Downloading...", font=("Arial", 10), bg="#263D42", fg="white")
        secondDownload.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        print("Downloading...")
        
        # ask the user where to save the file
        save_path = filedialog.askdirectory()

        # download the file to the selected directory
        stream.download(save_path)

        # remove secondDownload label
        secondDownload.destroy()

        # create thirdDownload label
        thirdDownload = tk.Label(root, text="Download complete!", font=("Arial", 10), bg="#263D42", fg="white")
        thirdDownload.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        
        print("Download complete!")
        root.after(3000, thirdDownload.destroy)

    except Exception as e:
        errorLabel = tk.Label(root, text="Error: Invalid link or unable to download video.", font=("Arial", 10), bg="#263D42", fg="red")
        errorLabel.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        root.after(3000, errorLabel.destroy)

h1 = tk.Label(root, text="Youtube Video Downloader", font=("Arial", 26), bg="#263D42", fg= "white")
h1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

label = tk.Label(root, text="Youtube link:", font=("Arial", 10), bg="#263D42", fg= "white")
label.place(relx=0.34, rely=0.36, anchor=tk.CENTER)

downloadLink = tk.Button(root, text="Download video", padx = 10, pady= 5, fg="white", bg="#263D42", command=download_video)
downloadLink.place(relx=0.5, rely=0.55, anchor=tk.CENTER)


text_box = tk.Entry(root, width=50)
text_box.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# link = text_box.get()




root.mainloop()
