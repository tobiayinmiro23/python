from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print('video downloaded successfully')

    except Exception as e:
        print(e)


# path = "c:\Users\ayinm\Desktop\course\python"
path = "c:/Users/ayinm/Desktop/course/python"
# url = 'https://youtube.com/shorts/acCjF7T_h2I?si=g_o6uSOpi4cTOxl-'
# url = 'https://www.youtube.com/watch?v=yd0Z5YAv8Hk'
# url = 'https://www.youtube.com/shorts/watch?si=UV16yGg4kdRmw4Vu'
# url = "https://youtu.be/GEAcs2B-kNc?si=UV16yGg4kdRmw4Vu"
# url = "https://www.youtube.com/watch?v=i-9mUDbGsEk&list=RDGEAcs2B-kNc"
# url = "https://youtu.be/i-9mUDbGsEk?si=UT7wsidvggKCQF-8"
url = "https://www.youtube.com/watch?v=i-9mUDbGsEk"
download_video(url, path)
# https://www.youtube.com/watch?v=NskTWCSmZt4
