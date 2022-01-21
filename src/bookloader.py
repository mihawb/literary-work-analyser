from urllib.request import urlopen
import json, os

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
    response = urlopen(url)
    return json.loads(response.read())

slugs = [
        'pan-tadeusz',
        'dziady-dziady-poema-dziady-czesc-iii',
        'dziady-dziady-poema-dziady-czesc-iv',
        'quo-vadis',
        'latarnik',
        'krzyzacy-tom-pierwszy',
        'krzyzacy-tom-drugi',
        'syzyfowe-prace',
        'ludzie-bezdomni-tom-pierwszy',
        'ludzie-bezdomni-tom-drugi',
        'przedwiosnie',
        'wesele',
        'noc-listopadowa',
        'wyspianski-akropolis',
        'deklaracja-praw-dziecka',
        'konwencja-o-prawach-dziecka',
        'deklaracja-praw-czlowieka',
        'kamizelka',
        'prus-dziwna-historia',
        'prus-powiastki-cmentarne',
        'pieklo-kobiet',
        'jak-skonczyc-z-pieklem-kobiet',
        'plotka-o-weselu-wyspianskiego',
        'julianka',
        'dobra-pani',
        'orzeszkowa-ascetka'
        ]

if __name__ == "__main__":
    if not os.path.isdir('../books'):
        os.mkdir('../books')
        
    errloghand = open('../bookloader_err.log', 'w', encoding = 'utf-8')
    errcount = 1

    for bookcount, slug in progressBar(slugs):
        
        book = getJSONfromURL(f'https://wolnelektury.pl/api/books/{slug}/')
        authorslug = book['authors'][0]['slug']

        try:
            response = urlopen(book['txt'])
            bhand = open(f'../books/{authorslug}_{slug}.txt', 'w', encoding = 'utf-8')

            for line in response.readlines():
                bhand.write(line.decode('utf-8').rstrip() + '\n')

            bhand.close()

        except Exception as e:
            errloghand.write(f'ERROR NO {errcount} | BOOK NO {bookcount} (1-based indexing)\n')
            errloghand.write(f'{e}\n')
            errloghand.write(f'API HREF: {book["href"]}\n')
            errloghand.write(f'Title: {book["title"]}\n')
            errloghand.write(f'Author: {book["author"]}\n\n')
            errcount += 1

    errloghand.close()