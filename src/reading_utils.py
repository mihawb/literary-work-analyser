import json
import os
import ssl
from urllib.request import urlopen

def progressBar(iterable, prefix = 'Progress:', suffix = 'Complete', decimals = 1, length = 50, fill = '█', printEnd = '\r'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    
    def printProgressBar (iteration):
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
    printProgressBar(0)
    
    for i, item in enumerate(iterable):
        yield i, item
        printProgressBar(i + 1)
    
    print()


def getJSONfromURL(url):
    gcontext = ssl.SSLContext()
    response = urlopen(url, context=gcontext)
    return json.loads(response.read())

def get_books_of_given_author(author):
    if not os.path.isdir('../books'):
        os.mkdir('../books')
        
    errloghand = open('../bookloader_err.log', 'w', encoding = 'utf-8')
    errcount = 1

    books = getJSONfromURL(f'https://wolnelektury.pl/api/authors/{author}/books/')

    for book in books:

        current_book = getJSONfromURL(book['href'])
        book_title = book['slug']

        try:
            gcontext = ssl.SSLContext()
            response = urlopen(current_book['txt'], context=gcontext)
            bhand = open(f'../books/{author}_{book_title}.txt', 'w', encoding = 'utf-8')

            for line in response.readlines():
                decoded = line.decode('utf-8').rstrip() + '\n'
                
                if decoded == '-----\n':
                    break

                bhand.write(decoded)

            bhand.close()

        except Exception as e:
            errloghand.write(f'ERROR NO {errcount}')
            errloghand.write(f'{e}\n')
            errloghand.write(f'API HREF: {book["href"]}\n')
            errloghand.write(f'Title: {book["title"]}\n')
            errloghand.write(f'Author: {book["author"]}\n\n')
            errcount += 1

    errloghand.close()
    

def get_books_according_to_slugs(slugs):    
    if not os.path.isdir('../books'):
        os.mkdir('../books')
        
    errloghand = open('../bookloader_err.log', 'w', encoding = 'utf-8')
    errcount = 1

    for bookcount, slug in progressBar(slugs):

        book = getJSONfromURL(f'https://wolnelektury.pl/api/books/{slug}/')
        authorslug = book['authors'][0]['slug']

        try:
            gcontext = ssl.SSLContext()
            response = urlopen(book['txt'], context=gcontext)
            bhand = open(f'../books/{authorslug}_{slug}.txt', 'w', encoding = 'utf-8')

            for line in response.readlines():
                decoded = line.decode('utf-8').rstrip() + '\n'
                
                if decoded == '-----\n':
                    break

                bhand.write(decoded)

            bhand.close()

        except Exception as e:
            errloghand.write(f'ERROR NO {errcount} | BOOK NO {bookcount} (1-based indexing)\n')
            errloghand.write(f'{e}\n')
            errloghand.write(f'API HREF: {book["href"]}\n')
            errloghand.write(f'Title: {book["title"]}\n')
            errloghand.write(f'Author: {book["author"]}\n\n')
            errcount += 1

    errloghand.close()
    
def get_books_of_given_epochs(epochs):
    if not os.path.isdir('../books'):
        os.mkdir('../books')
        
    errloghand = open('../bookloader_err.log', 'w', encoding = 'utf-8')
    errcount = 1

    books = getJSONfromURL(f'https://wolnelektury.pl/api/epochs/{epochs}/books/')

    for book in books:

        current_book = getJSONfromURL(book['href'])
        book_title = book['slug']
        author = current_book['authors'][0]['slug']

        try:
            gcontext = ssl.SSLContext()
            response = urlopen(current_book['txt'], context=gcontext)
            bhand = open(f'../books/{author}_{book_title}.txt', 'w', encoding = 'utf-8')

            for line in response.readlines():
                decoded = line.decode('utf-8').rstrip() + '\n'
                
                if decoded == '-----\n':
                    break

                bhand.write(decoded)

            bhand.close()

        except Exception as e:
            errloghand.write(f'ERROR NO {errcount}')
            errloghand.write(f'{e}\n')
            errloghand.write(f'API HREF: {book["href"]}\n')
            errloghand.write(f'Title: {book["title"]}\n')
            errloghand.write(f'Author: {book["author"]}\n\n')
            errcount += 1

    errloghand.close()
    