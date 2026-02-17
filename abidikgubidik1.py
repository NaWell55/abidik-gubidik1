import tkinter as tk

pencere = tk.Tk()
pencere.attributes("-fullscreen", True)
pencere.configure(bg="blue")

yazi = tk.Label(
    pencere,
    text=":(\nBilgisayarınız bir sorunla karşılaştı ve yeniden başlatılması gerekiyor.\n\n%100 tamamlandı",
    fg="white",
    bg="blue",
    font=("Consolas", 24),
    justify="left"
)

yazi.pack(padx=50, pady=50, anchor="nw")

pencere.bind("<Escape>", lambda e: pencere.destroy())  # ESC ile kapanır
pencere.mainloop()