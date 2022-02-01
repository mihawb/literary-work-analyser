import os, fnmatch, random
from authorwordbag import WordBagOfAuthorClassifier
from bookwordbag import WordBagOfOneBookClassifier

def sedzia(klasyfikator, zbior_ksiazek, ilosc_testow, ilosc_linii, seed=0, lim=0):
    defaultbookpath = '..\\books'
    if lim == 0:
        K = klasyfikator(zbior_ksiazek)
    else:
        K = klasyfikator(zbior_ksiazek, lim)

    rauthors = []
    rfrags = []
    rodps = []
    rbooks = []

    books = dict()
    random.seed(seed)
    authors = K.getAuthors()

    paths = []
    for author in authors:
        for root, dirs, files in os.walk(defaultbookpath):
            for name in files:
                if fnmatch.fnmatch(name, author + '_*.txt'):
                    paths.append(os.path.join(root, name))

    for path in paths:
        with open(path, 'r', encoding='utf-8') as book:
            dtidx = path.index('.', len(defaultbookpath)+1)
            title = path[len(defaultbookpath)+1:dtidx]
            books[title] = []

            for line in book:
                line = line.strip().lower()
                if line:
                    books[title].append(line)
    
    for t in range(ilosc_testow):
        b = random.choice(list(books.keys()))                   # ksiazka
        l = random.randint(1, min(ilosc_linii, len(books[b])))  # linie
        s = random.randint(0, max(0, min(ilosc_linii, len(books[b])) - ilosc_linii))      # index startu od ktorej linii zaczyna sie fragment
        # to zapewnia ze s bedzie z przedzialu [0, len(b) - i_l] => nie mieszamy w pamieci
        a = b[:b.index('_')]                                    # autor
        f = ''                                                  # generowany fragment

        rauthors.append(a)
        rbooks.append(b)
        for i in range(l):
            f += books[b][s + i] + ' '
        f = f.strip()
        rfrags.append(f)

    for t in range(ilosc_testow):
        odp = K.classify(rfrags[t])
        rodps.append(odp)

    return rauthors, rbooks, rfrags, rodps

    # rauthors (list of str)    - lista faktycznych autorow danych fragmentow               - zapisane jako author_slug
    # rbooks (list of str)      - lista ksiazek z ktorych pochodza dane fragmenty           - zapisane jako author_title_slug
    # rfrags (list of str)      - lista fargmentow w formie stringow                        - doslownie fragmenty ksiazek ale, zapisane bez znakow nowej linii
    # rodps (list of str)       - lista autorow jakie klasyfikator przypisal danemu frag.   - zapisane jako author_slug


if __name__ == "__main__":
    # AWB potrzebuje: '..\\books', limitu
    # BWB potrzebuje: '..\\zb_uczacy'

    # a, b, f, r = sedzia(WordBagOfAuthorClassifier, '..\\books', 10, 100, 1337, 200)
    a, b, f, r = sedzia(WordBagOfOneBookClassifier, '..\\zb_uczacy', 10, 100, 1234)

    for i in range(10):
        print(a[i], r[i], a[i] == r[i], b[i])
