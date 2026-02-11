import tkinter as tk
from tkinter import messagebox
import os
import requests


def get_ext(url: str) -> str | None:
    exts = [".png", ".jpeg", ".jpg"]
    for ext in exts:
        if ext in url:
            return ext
    return None


def download_img():
    url = url_ent.get()
    file_name = name_ent.get()
    folder_path = folder_ent.get()

    if not url or not file_name or not folder_path:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    ext = get_ext(url)
    if not ext:
        messagebox.showerror("Error", "Invalid image URL.")
        return

    img_path = os.path.join(folder_path, f"{file_name}{ext}")

    if os.path.isfile(img_path):
        messagebox.showerror(
            "Error", "A file with the same name already exists.")
        return

    try:
        img_content = requests.get(u).content
        with open(img_path, "wb") as handler:
            handler.write(img_content)
            messagebox.showinfo("Success", f"Image downloaded to:\n{img_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("Image Downloader")
root.configure(bg="#1e1e1e")

ul = tk.Label(root, text="Image URL:", bg="#1e1e1e", fg="white")
ul.pack(pady=5)

url_ent = tk.Entry(root, width=50)
url_ent.pack(pady=5)

nl = tk.Label(root, text="Image Name:", bg="#1e1e1e", fg="white")
nl.pack(pady=5)

name_ent = tk.Entry(root, width=50)
name_ent.pack(pady=5)

fl = tk.Label(root, text="Folder Path:", bg="#1e1e1e", fg="white")
fl.pack(pady=5)

folder_ent = tk.Entry(root, width=50)
folder_ent.pack(pady=5)

dl_btn = tk.Button(root, text="Download",
                   command=download_img, bg="#303030", fg="white")
dl_btn.pack(pady=10)

root.mainloop()
