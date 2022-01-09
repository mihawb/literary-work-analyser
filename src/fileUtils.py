def readFileContent(path, array):

    words = []
    with open(path, 'r') as file:
        for line in file:
            for word in line.split():
                print(word)
                array.append(word)
