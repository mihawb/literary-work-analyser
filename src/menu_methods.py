from tkinter import filedialog as fd
from tkinter import messagebox


# Selecting file
def select_file(array_with_word):
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    path = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    read_file_content(path, array_with_word)


# Reading word from file to given array
def read_file_content(path, array_with_word):
    array_with_word.clear()
    with open(path, 'r') as file:
        for line in file:
            for word in line.split():
                array_with_word.append(word)


def analize(array_with_word):
    if len(array_with_word) == 0:
        messagebox.showwarning("Błąd", "Brak słów do analizy")

    for word in array_with_word:
        print(word)
        # TODO cała mechanika znajdywnia tekstu