import os, fnmatch
class WordBagOfOneBookClassifier:
    __unnecessary_chars = ["!",",",".","    ",":",";","?","(",")","—","*","»","…","«","—","-","„","”",'"',"°","'"] 
    __stops = ['a', 'aby', 'ach', 'acz', 'aczkolwiek', 'aj', 'albo', 'ale', 'alez', 'ależ', 'ani', 'az', 'aż', 'bardziej', 'bardzo', 'beda', 'bedzie', 'bez', 'deda', 'będą', 'bede', 'będę', 'będzie', 'bo', 'bowiem', 'by', 'byc', 'być', 'byl', 'byla', 'byli', 'bylo', 'byly', 'był', 'była', 'było', 'były', 'bynajmniej', 'cala', 'cali', 'caly', 'cała', 'cały', 'ci', 'cie', 'ciebie', 'cię', 'co', 'cokolwiek', 'cos', 'coś', 'czasami', 'czasem', 'czemu', 'czy', 'czyli', 'daleko', 'dla', 'dlaczego', 'dlatego', 'do', 'dobrze', 'dokad', 'dokąd', 'dosc', 'dość', 'duzo', 'dużo', 'dwa', 'dwaj', 'dwie', 'dwoje', 'dzis', 'dzisiaj', 'dziś', 'gdy', 'gdyby', 'gdyz', 'gdyż', 'gdzie', 'gdziekolwiek', 'gdzies', 'gdzieś', 'go', 'i', 'ich', 'ile', 'im', 'inna', 'inne', 'inny', 'innych', 'iz', 'iż', 'ja', 'jak', 'jakas', 'jakaś', 'jakby', 'jaki', 'jakichs', 'jakichś', 'jakie', 'jakis', 'jakiś', 'jakiz', 'jakiż', 'jakkolwiek', 'jako', 'jakos', 'jakoś', 'ją', 'je', 'jeden', 'jedna', 'jednak', 'jednakze', 'jednakże', 'jedno', 'jego', 'jej', 'jemu', 'jesli', 'jest', 'jestem', 'jeszcze', 'jeśli', 'jezeli', 'jeżeli', 'juz', 'już', 'kazdy', 'każdy', 'kiedy', 'kilka', 'kims', 'kimś', 'kto', 'ktokolwiek', 'ktora', 'ktore', 'ktorego', 'ktorej', 'ktory', 'ktorych', 'ktorym', 'ktorzy', 'ktos', 'ktoś', 'która', 'które', 'którego', 'której', 'który', 'których', 'którym', 'którzy', 'ku', 'lat', 'lecz', 'lub', 'ma', 'mają', 'mało', 'mam', 'mi', 'miedzy', 'między', 'mimo', 'mna', 'mną', 'mnie', 'moga', 'mogą', 'moi', 'moim', 'moj', 'moja', 'moje', 'moze', 'mozliwe', 'mozna', 'może', 'możliwe', 'można', 'mój', 'mu', 'musi', 'my', 'na', 'nad', 'nam', 'nami', 'nas', 'nasi', 'nasz', 'nasza', 'nasze', 'naszego', 'naszych', 'natomiast', 'natychmiast', 'nawet', 'nia', 'nią', 'nic', 'nich', 'nie', 'niech', 'niego', 'niej', 'niemu', 'nigdy', 'nim', 'nimi', 'niz', 'niż', 'no', 'o', 'obok', 'od', 'około', 'on', 'ona', 'one', 'oni', 'ono', 'oraz', 'oto', 'owszem', 'pan', 'pana', 'pani', 'po', 'pod', 'podczas', 'pomimo', 'ponad', 'poniewaz', 'ponieważ', 'powinien', 'powinna', 'powinni', 'powinno', 'poza', 'prawie', 'przeciez', 'przecież', 'przed', 'przede', 'przedtem', 'przez', 'przy', 'roku', 'rowniez', 'również', 'sam', 'sama', 'są', 'sie', 'się', 'skad', 'skąd', 'soba', 'sobą', 'sobie', 'sposob', 'sposób', 'swoje', 'ta', 'tak', 'taka', 'taki', 'takie', 'takze', 'także', 'tam', 'te', 'tego', 'tej', 'ten', 'teraz', 'też', 'to', 'toba', 'tobą', 'tobie', 'totez', 'toteż', 'totobą', 'trzeba', 'tu', 'tutaj', 'twoi', 'twoim', 'twoj', 'twoja', 'twoje', 'twój', 'twym', 'ty', 'tych', 'tylko', 'tym', 'u', 'w', 'wam', 'wami', 'was', 'wasz', 'wasza', 'wasze', 'we', 'według', 'wiele', 'wielu', 'więc', 'więcej', 'wlasnie', 'właśnie', 'wszyscy', 'wszystkich', 'wszystkie', 'wszystkim', 'wszystko', 'wtedy', 'wy', 'z', 'za', 'zaden', 'zadna', 'zadne', 'zadnych', 'zapewne', 'zawsze', 'ze', 'zeby', 'zeznowu', 'zł', 'znow', 'znowu', 'znów', 'zostal', 'został', 'żaden', 'żadna', 'żadne', 'żadnych', 'że', 'żeby']
        
    def __findBooksPaths(self) -> list:
        result = []
        for root, dirs, files in os.walk(self.__booksRelPath):
            for name in files:
                if fnmatch.fnmatch(name, '*_*.txt'):
                    result.append(os.path.join(root, name))
        return result
    
    def __buildTokenDict(self, path) -> dict:
        '''
        Builds anew or expands book's or author's word bag.
        @params:
            path     - Required : valid path to a book in txt format (Str)
        '''
        wordbag = dict()
        tokens_stop = []
        tokens = []

        with open(path, 'r', encoding='utf-8') as book:
            for line in book:        
                for char in self.__unnecessary_chars:
                    line = line.replace(char, '')
                line = line.rstrip().lower().split()

                if line:
                    tokens_stop.extend(line)

        for ts in tokens_stop:
            if not ts in self.__stops:
                tokens.append(ts)

        for word in sorted(tokens):
            if word.isalpha():
                wordbag[word] = wordbag.get(word, 0) + 1

        return wordbag
    
    def __buildTokenSet(self, frag) -> list:
        '''
        Builds token set for specified text.
        @params:
            frag     - Required : literary work fragment for analysis (Str)
        '''
        frag = frag.replace('\n', ' ')
        for char in self.__unnecessary_chars:
            frag = frag.replace(char, '')
        frag = frag.strip().lower().split()

        tokens = []
        for token in frag:
            if token not in tokens and token not in self.__stops:
                tokens.append(token)

        return tokens
    
    def __buildBooksWB(self) -> None:
        self.__booksWB = dict()
        
        paths = self.__findBooksPaths()

        for p in paths:
            dtidx = p.index('.', len(self.__booksRelPath)+1)
            title = p[len(self.__booksRelPath)+1:dtidx]
            self.__booksWB[title] = self.__buildTokenDict(p)

            usidx = p.index('_', len(self.__booksRelPath)+1)
            author = p[len(self.__booksRelPath)+1:usidx]
            if author not in self.authors:
                self.authors.append(author)
    
    def __buildClassifier(self) -> None:
        self.__authorTotal = dict()
        self.__authorScore = dict()

        for book in self.__booksWB:
            usidx = book.index('_')
            author = book[:usidx]
            self.__authorTotal[author] = self.__authorTotal.get(author, 0)
            self.__authorScore[author] = self.__authorScore.get(author, 0)

            for token in self.__booksWB[book]:
                self.__authorTotal[author] += self.__booksWB[book][token]
    
    def __clearScore(self) -> None:
        for author in self.authors:
            self.__authorScore[author] = 0
    
    def __prepareClassification(self, frag) -> None:
        self.__clearScore()
        fragtokens = self.__buildTokenSet(frag)
        
        for book in self.__booksWB:
            usidx = book.index('_')
            author = book[:usidx]
            for token in fragtokens:
                self.__authorScore[author] += self.__booksWB[book].get(token, 0)
                # TODO to zamienic na ifa i dodac ze jesli trafienie to liczba_traf++
                # i potem zwracamy srednia = total / liczba_traf
                
    def classifyFullProb(self, frag) -> dict:
        self.__prepareClassification(frag)
        result = dict()
        for author in self.__authorScore:
            result[author] = self.__authorScore[author] / self.__authorTotal[author] * 100

        return result
    
    def classify(self, frag) -> str:
        full = self.classifyFullProb(frag)
        maxa = ""
        maxi = 0
        for author in self.authors:
            if full[author] > maxi:
                maxi = full[author]
                maxa = author
        return maxa

    def getAuthors(self) -> list:
        return self.authors
        
    def __init__(self, booksRelPath) -> None:
        self.authors = []
        self.__booksRelPath = booksRelPath
        
        self.__buildBooksWB()
        self.__buildClassifier()

# TODO moze przy klasyfykacji zbierac tez info o sredniej ilosci wystapien tokenu,
# a nie tylko o sumie wystapien dla wszystkich tokenow fragmentu?

# WordBagOfOneBookClassifier - do zadanego fragmentu autor jest dopasowywany na podstawie wszystkich tokenow z tylko jednej ksiazki autora
# ewaluacja - wynik dopasowania = suma wystapien trafionych tokenow we fragmencie / suma wystapien wszystkich tokenow autora - wybierany jest autor o najwiekszej nocie 
# natomiast moze lepiej byloby dac cos logarytmicznego wzgledem ilosci wszystkich tokenow??

# pola:
# __booksRelPath (str)  - sciezka do zbioru uczacego, tj folderu z pojedynczymi ksiazkami roznych autorow           - na nich kompilowany jest klasyfikator
# __booksWB (dict)      - mapa <author_title_slug : worek_slow>, gdzie worek_slow to mapa <token : ilosc_wystapien> - zawiera wszystkie tokeny z pojedynczych dziel
# authors (list)        - lista slugow autorow zawartych w zbiorze uczacym
# __authorTotal (dict)  - mapa <author_slug : laczna_ilosc_wystapien_wszystkich_tokenow>                            - potrzebne do ewaluacji 
# __authorScore (dict)  - mapa <author_slug : suma_wystapien_tokenow_autora_we_fragmencie>                          - potrzebne do ewaluacji

# metody publiczne:
# getAuthors() -> list              - zwraca liste wszytkich kategorii (autorow) skompilowanego klasyfikatora
# classify(frag) -> str             - zwraca autora dopasowanego do fragmentu utworu
# classifyFullProb(frag) -> dict    - zwraca mape <author_slug : wynik_dopasowania> czyli wyniki dopasowania do fragmentu dla wszystkich autorow, przydatne raczej do debugu 
