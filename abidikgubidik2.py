import tkinter as tk
import random

p = tk.Tk()
p.title("Beni yakala")
p.geometry("200x100")

def kac(event=None):
    x = random.randint(0, 1000)
    y = random.randint(0, 600)
    p.geometry(f"200x100+{x}+{y}")

def kapatma_engel():
    pass  

btn = tk.Button(p, text="Kapat")
btn.pack(expand=True)

btn.bind("<Enter>", kac)
p.protocol("WM_DELETE_WINDOW", kapatma_engel)  
p.bind("<Escape>", lambda e: p.destroy())      

p.mainloop()