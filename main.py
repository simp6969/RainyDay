try:
    import requests
    import tkinter as tk
    from PIL import Image, ImageTk
    import io
    import os
    from colorama import init, Fore
except ModuleNotFoundError:
    print(Fore.RED + "[ERROR] Module Not Found" + Fore.RESET)


def load_link(value):
    os.startfile(value)


init(convert=True)

root = tk.Tk()
root.title("Link Loader")
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

for line in range(5):
    link = "https://wholesomelist.com/api/random/"
    ans = requests.get(link)
    data = ans.json()
    value2 = data["entry"]["title"]
    value = data["entry"]["link"]
    image = data["entry"]["image"]
    print(Fore.YELLOW + "[INFO] fetching links: " + value + Fore.RESET)

    var = value
    button = tk.Button(frame, text=var, command=lambda v=var: load_link(v))
    label1 = tk.Label(frame, text=value2)

    image_data = requests.get(image).content
    image1 = Image.open(io.BytesIO(image_data))
    image1 = image1.resize((125, 150))
    img = ImageTk.PhotoImage(image1)
    photo = tk.Label(frame, image=img)
    photo.image = img

    button.grid(row=line, column=0, padx=5, pady=5, sticky="w")
    label1.grid(row=line, column=1, padx=5, pady=5, sticky="w")
    photo.grid(row=line, column=2, padx=5, pady=5, sticky="w")


root.mainloop()
