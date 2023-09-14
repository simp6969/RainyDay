import requests
import tkinter as tk
import os


def load_link(value):
    os.startfile(value)


root = tk.Tk()
root.title("Link Loader")

for line in range(10):
    link = "https://wholesomelist.com/api/random/"
    ans = requests.get(link)
    data = ans.json()
    value2 = data["entry"]["title"]
    value = data["entry"]["link"]
    print("[INFO] fetching links: " + value)

    var = value
    button = tk.Button(root, text=var, command=lambda v=var: load_link(v))
    label1 = tk.Label(root, text=value2)

    label1.pack()
    button.pack()

root.mainloop()
