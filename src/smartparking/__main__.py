import tkinter as tk
from .vista.aplicacion import AplicacionEscritorio

def main():
    root = tk.Tk()
    app = AplicacionEscritorio(root)
    root.mainloop()

if __name__ == "__main__":
    main()
