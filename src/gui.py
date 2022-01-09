import tkinter as tk
from tkinter import ttk

from src.bookloader import scrap_data
from src.menu_methods import select_file, analize

array_with_word = []


# Main class with whole GUI
class MainWindow:
    def __init__(self, win):
        self.lbl1 = tk.Label(win, text='Wyszukiwanie dzieła na podstawie słów', font="none 14 bold", padx=40, pady=40)
        self.lbl1.grid(column=0, row=0)

        self.lbl2 = tk.Label(win, text='Wczytaj dzieła ze strony', font="none 12")
        self.lbl2.grid(column=0, row=1)

        # Button with loading text from web
        self.load_button = tk.Button(
            window,
            text="Wczytaj",
            command=lambda: scrap_data())

        self.load_button.grid(column=0, row=3)

        # Empty space
        self.lbl4 = tk.Label(win, text='', font="none 12", padx=10, pady=10)
        self.lbl4.grid(column=0, row=4)

        # Button with picking file with words to analize
        self.lbl3 = tk.Label(win, text='Wczytaj plik txt ze słowami', font="none 12")
        self.lbl3.grid(column=0, row=5)

        self.open_button = ttk.Button(
            win,
            text='Wybierz plik',
            command=lambda: select_file(array_with_word)
        )
        self.open_button.grid(column=0, row=6)

        # Empty space
        self.lbl4 = tk.Label(win, text='', font="none 12", padx=10, pady=10)
        self.lbl4.grid(column=0, row=7)

        self.lbl3 = tk.Label(win, text='Dokonaj analizy na podstawie słów', font="none 12")
        self.lbl3.grid(column=0, row=8)

        # Main program, analizing data with given array of words
        self.analize_button = ttk.Button(
            win,
            text='Analizuj',
            command=lambda: analize(array_with_word)
        )
        self.analize_button.grid(column=0, row=9)

        self.lbl5 = tk.Label(win, text='Dalsze operacje...', font="none 12", padx=40, pady=40)
        self.lbl5.grid(column=0, row=11)

# Running program
window = tk.Tk()
window.title('Text searcher')
window.resizable(False, False)
mainWindow = MainWindow(window)
window.mainloop()
