# Reading word from file to givne array
def read_file_content(path, array):
    with open(path, 'r') as file:
        for line in file:
            for word in line.split():
                array.append(word)
