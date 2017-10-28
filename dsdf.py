#-*- encoding: utf-8 -*-
import subprocess
import tkinter as tk
from os import *
import os
import time

root = tk.Tk()

def my_function():
    current_query = my_entry.get()
    url_member_1 = "http://www.google.com/search\?q\="+ str(current_query) + "\&source\=lnms\&tbm\=isch"
    url_member_2 = "http://www.google.com/search\?q\=" + str(current_query) + str(current_query) + "\&source\=lnms\&tbm\=isch"

    os.system("chrome-cli open "+ url_member_1 + " -t 191")
    os.system("chrome-cli open "+ url_member_2 + " -t 37")
    time.sleep(3)
    os.system("screencapture ~/Desktop/photo_folder/" + current_query + "_1.png " + "~/Desktop/photo_folder/" + current_query  + "_2.png "  + "~/Desktop/photo_folder/" + current_query  + "_3.png")
    time.sleep(3)
    os.system("lp -d Canon_MP250_series_2 "+ "~/Desktop/photo_folder/" + current_query + "_2.png")
    os.system("lp -d Canon_MP250_series_2 "+ "~/Desktop/photo_folder/" + current_query + "_3.png")
    


photo = tk.PhotoImage(file="googlelogo-ConvertImage.gif")
photo = photo.subsample(2, 2)
r = tk.Label(root, image=photo)
r.place(relx=0.38, rely=0.4)

my_entry = tk.Entry(root, width=40)
my_entry.place(relx=0.355, rely=0.54)

my_button = tk.Button(root, text = "Submit", command = my_function)
my_button.place(relx=0.605, rely = 0.54)


root.mainloop()

