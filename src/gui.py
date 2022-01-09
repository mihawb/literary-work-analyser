import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

from src.bookloader import scrap_data
from src.fileUtils import read_file_content

arrayWithWord = []


# Selecting file
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    path = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    read_file_content(path, arrayWithWord)


def analize():
    if len(arrayWithWord) == 0:
        messagebox.showwarning("Błąd", "Brak słów do analizy")

    for word in arrayWithWord:
        print(word)
        # TODO cała mechanika znajdywnia tekstu


# Main class with whole GUI
class MainWindow:
    def __init__(self, win):
        self.lbl1 = tk.Label(win, text='Wyszukiwanie dzieła na podstawie słów', font="none 14 bold", padx=40, pady=40)
        self.lbl1.grid(column=0, row=0)

        self.lbl2 = tk.Label(win, text='Wczytaj dzieła ze strony', font="none 12")
        self.lbl2.grid(column=0, row=1)

        self.load_button = tk.Button(
            window,
            text="Wczytaj",
            command=scrap_data)

        self.load_button.grid(column=0, row=3)

        # Empty space
        self.lbl4 = tk.Label(win, text='', font="none 12", padx=10, pady=10)
        self.lbl4.grid(column=0, row=4)

        self.lbl3 = tk.Label(win, text='Wczytaj plik txt ze słowami', font="none 12")
        self.lbl3.grid(column=0, row=5)

        self.open_button = ttk.Button(
            win,
            text='Wybierz plik',
            command=select_file
        )
        self.open_button.grid(column=0, row=6)

        # Empty space
        self.lbl4 = tk.Label(win, text='', font="none 12", padx=10, pady=10)
        self.lbl4.grid(column=0, row=7)

        self.lbl3 = tk.Label(win, text='Dokonaj analizy na podstawie słów', font="none 12")
        self.lbl3.grid(column=0, row=8)

        self.analize_button = ttk.Button(
            win,
            text='Analizuj',
            command=analize
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
