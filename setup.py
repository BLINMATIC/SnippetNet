import requests
import tkinter as tk
import os

root = tk.Tk()
root.title("SnippetNet installer")
root.resizable(False, False)

label = tk.Label(root, text="Enter the type of installation")
label.pack()

radio_var = tk.IntVar()
radio_var.set(1)
radio_button = tk.Radiobutton(root, text="Install Server", variable=radio_var, value=1)
radio_button.pack()
radio_button = tk.Radiobutton(root, text="Install Client", variable=radio_var, value=2)
radio_button.pack()

label = tk.Label(root, text="Path")
label.pack()

path = tk.Text(root, height=1, width=20)
path.pack()

install = tk.Button(root, text="Install", command=lambda: install_snippetnet(radio_var.get(), path.get("1.0", "end-1c")))
install.pack()


def install_snippetnet(type, path):
    if type == 1:
        os.chdir(path)
        open("__main__.py", "w").write(requests.get("https://raw.githubusercontent.com/BLINMATIC/SnippetNet/main/client/__main__.py").text)
        open("config.py", "w").write(requests.get("https://raw.githubusercontent.com/BLINMATIC/SnippetNet/main/client/config.py").text)
    elif type == 2:
        os.chdir(path)
        open("__main__.py", "w").write(requests.get("https://raw.githubusercontent.com/BLINMATIC/SnippetNet/main/server/__main__.py").text)
        open("config.py", "w").write(requests.get("https://raw.githubusercontent.com/BLINMATIC/SnippetNet/main/server/config.py").text)

root.mainloop()