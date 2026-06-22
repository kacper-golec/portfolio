import tkinter as tk

def kliknij(symbol):
    aktualne = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, aktualne + symbol)

def oblicz():
    try:
        wynik = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(wynik))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Błąd")

def wyczysc():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Kalkulator")
root.geometry("320x370")     
root.resizable(False, False) 

entry = tk.Entry(root, font=("Arial", 24),bg="#ffffff", justify="right", bd=4)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

przyciski = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

for (text, row, col) in przyciski:
    if text == "=":
        tk.Button(root, text=text, font=("Arial", 18),bg="#FFFB00", command=oblicz)\
            .grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    else:
        tk.Button(root, text=text, font=("Arial", 18),bg="#64cd41",
                  command=lambda t=text: kliknij(t))\
            .grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

tk.Button(root, text="C", font=("Arial", 18), command=wyczysc)\
    .grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

root.mainloop()