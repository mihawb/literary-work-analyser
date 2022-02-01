import os, fnmatch
class WordBagOfAuthorClassifier:
    __unnecessary_chars = ["!",",",".","    ",":",";","?","(",")","—","*","»","…","«","—","-","„","”",'"',"°","'"] 
    __stops = ['a', 'aby', 'ach', 'acz', 'aczkolwiek', 'aj', 'albo', 'ale', 'alez', 'ależ', 'ani', 'az', 'aż', 'bardziej', 'bardzo', 'beda', 'bedzie', 'bez', 'deda', 'będą', 'bede', 'będę', 'będzie', 'bo', 'bowiem', 'by', 'byc', 'być', 'byl', 'byla', 'byli', 'bylo', 'byly', 'był', 'była', 'było', 'były', 'bynajmniej', 'cala', 'cali', 'caly', 'cała', 'cały', 'ci', 'cie', 'ciebie', 'cię', 'co', 'cokolwiek', 'cos', 'coś', 'czasami', 'czasem', 'czemu', 'czy', 'czyli', 'daleko', 'dla', 'dlaczego', 'dlatego', 'do', 'dobrze', 'dokad', 'dokąd', 'dosc', 'dość', 'duzo', 'dużo', 'dwa', 'dwaj', 'dwie', 'dwoje', 'dzis', 'dzisiaj', 'dziś', 'gdy', 'gdyby', 'gdyz', 'gdyż', 'gdzie', 'gdziekolwiek', 'gdzies', 'gdzieś', 'go', 'i', 'ich', 'ile', 'im', 'inna', 'inne', 'inny', 'innych', 'iz', 'iż', 'ja', 'jak', 'jakas', 'jakaś', 'jakby', 'jaki', 'jakichs', 'jakichś', 'jakie', 'jakis', 'jakiś', 'jakiz', 'jakiż', 'jakkolwiek', 'jako', 'jakos', 'jakoś', 'ją', 'je', 'jeden', 'jedna', 'jednak', 'jednakze', 'jednakże', 'jedno', 'jego', 'jej', 'jemu', 'jesli', 'jest', 'jestem', 'jeszcze', 'jeśli', 'jezeli', 'jeżeli', 'juz', 'już', 'kazdy', 'każdy', 'kiedy', 'kilka', 'kims', 'kimś', 'kto', 'ktokolwiek', 'ktora', 'ktore', 'ktorego', 'ktorej', 'ktory', 'ktorych', 'ktorym', 'ktorzy', 'ktos', 'ktoś', 'która', 'które', 'którego', 'której', 'który', 'których', 'którym', 'którzy', 'ku', 'lat', 'lecz', 'lub', 'ma', 'mają', 'mało', 'mam', 'mi', 'miedzy', 'między', 'mimo', 'mna', 'mną', 'mnie', 'moga', 'mogą', 'moi', 'moim', 'moj', 'moja', 'moje', 'moze', 'mozliwe', 'mozna', 'może', 'możliwe', 'można', 'mój', 'mu', 'musi', 'my', 'na', 'nad', 'nam', 'nami', 'nas', 'nasi', 'nasz', 'nasza', 'nasze', 'naszego', 'naszych', 'natomiast', 'natychmiast', 'nawet', 'nia', 'nią', 'nic', 'nich', 'nie', 'niech', 'niego', 'niej', 'niemu', 'nigdy', 'nim', 'nimi', 'niz', 'niż', 'no', 'o', 'obok', 'od', 'około', 'on', 'ona', 'one', 'oni', 'ono', 'oraz', 'oto', 'owszem', 'pan', 'pana', 'pani', 'po', 'pod', 'podczas', 'pomimo', 'ponad', 'poniewaz', 'ponieważ', 'powinien', 'powinna', 'powinni', 'powinno', 'poza', 'prawie', 'przeciez', 'przecież', 'przed', 'przede', 'przedtem', 'przez', 'przy', 'roku', 'rowniez', 'również', 'sam', 'sama', 'są', 'sie', 'się', 'skad', 'skąd', 'soba', 'sobą', 'sobie', 'sposob', 'sposób', 'swoje', 'ta', 'tak', 'taka', 'taki', 'takie', 'takze', 'także', 'tam', 'te', 'tego', 'tej', 'ten', 'teraz', 'też', 'to', 'toba', 'tobą', 'tobie', 'totez', 'toteż', 'totobą', 'trzeba', 'tu', 'tutaj', 'twoi', 'twoim', 'twoj', 'twoja', 'twoje', 'twój', 'twym', 'ty', 'tych', 'tylko', 'tym', 'u', 'w', 'wam', 'wami', 'was', 'wasz', 'wasza', 'wasze', 'we', 'według', 'wiele', 'wielu', 'więc', 'więcej', 'wlasnie', 'właśnie', 'wszyscy', 'wszystkich', 'wszystkie', 'wszystkim', 'wszystko', 'wtedy', 'wy', 'z', 'za', 'zaden', 'zadna', 'zadne', 'zadnych', 'zapewne', 'zawsze', 'ze', 'zeby', 'zeznowu', 'zł', 'znow', 'znowu', 'znów', 'zostal', 'został', 'żaden', 'żadna', 'żadne', 'żadnych', 'że', 'żeby']

    def __findBooksPaths(self) -> list:
        result = []
        for root, dirs, files in os.walk(self.__booksRelPath):
            for name in files:
                if fnmatch.fnmatch(name, '*_*.txt'):
                    result.append(os.path.join(root, name))
        return result

    def __retrieveTokensFromBook(self, path) -> None:
        usidx = path.index('_', len(self.__booksRelPath)+1)
        author = path[len(self.__booksRelPath)+1:usidx]

        self.__authorsWB[author] = self.__authorsWB.get(author, dict())
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
                self.__authorsWB[author][word] = self.__authorsWB[author].get(word, 0) + 1

    def __truncateAuthorsWB(self) -> None:
        for author in self.__authorsWB:
            tempWB = dict(sorted(self.__authorsWB[author].items(), key=lambda x: x[1], reverse = True))
            self.__authorsWB[author] = dict()

            count = min(len(tempWB.keys()), self.__lim)
            for token in tempWB:
                self.__authorsWB[author][token] = tempWB[token]

                if count < 0: break
                count -= 1
                
    def __buildAuthorsWB(self) -> None:
        paths = self.__findBooksPaths()
        for p in paths:
            self.__retrieveTokensFromBook(p)
        self.__truncateAuthorsWB()

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

    def __buildClassifier(self) -> None:
        self.__authorTotal = dict([(a, 0) for a in self.__authorsWB])
        self.__authorScore = dict([(a, 0) for a in self.__authorsWB])

        for author in self.__authorsWB:
            for token in self.__authorsWB[author]:
                self.__authorTotal[author] += self.__authorsWB[author][token]

    def __clearScore(self) -> None:
        for author in self.__authorsWB:
            self.__authorScore[author] = 0

    def __prepareClassification(self, frag) -> None:
        self.__clearScore()
        fragtokens = self.__buildTokenSet(frag)

        for author in self.__authorsWB:
            for token in fragtokens:
                self.__authorScore[author] += self.__authorsWB[author].get(token, 0)

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
        for author in self.__authorsWB:
            if full[author] > maxi:
                maxi = full[author]
                maxa = author
        return maxa

    def getAuthors(self) -> list:
        return self.__authorsWB.keys()

    def __init__(self, booksRelPath, lim) -> None:
        self.__booksRelPath = booksRelPath
        self.__lim = lim
        self.__authorsWB = dict()

        self.__buildAuthorsWB()
        self.__buildClassifier()

# WordBagOfAuthorClassifier - do zadanego fragmentu autor jest dopasowywany na podstawie tylko najczestszych tokenow z calej puli dziel 
# ewaluacja - wynik dopasowania = suma wystapien trafionych tokenow we fragmencie / suma wystapien wszystkich tokenow autora - wybierany jest autor o najwiekszej nocie 
# natomiast moze lepiej byloby dac cos logarytmicznego wzgledem ilosci wszystkich tokenow??

# pola:
# __booksRelPath (str)  - sciezka do zbioru wszystkich ksiazek wszystkich autorow                               - na nich kompilowany jest klasyfikator
# __lim (int)           - liczba najczestszych tokenow dla kazdego autora
# __authorsWB (dict)    - mapa <author_slug : worek_slow>, gdzie worek_slow to mapa <token : ilosc_wystapien>   - zawiera najczestsze tokeny ze wszystkich dziel dla wszystkich autorow
# __authorTotal (dict)  - mapa <author_slug : laczna_ilosc_wystapien_wszystkich_tokenow>                        - potrzebne do ewaluacji 
# __authorScore (dict)  - mapa <author_slug : suma_wystapien_tokenow_autora_we_fragmencie>                      - potrzebne do ewaluacji

# metody publiczne:
# getAuthors() -> list              - zwraca liste wszytkich kategorii (autorow) skompilowanego klasyfikatora
# classify(frag) -> str             - zwraca autora dopasowanego do fragmentu utworu
# classifyFullProb(frag) -> dict    - zwraca mape <author_slug : wynik_dopasowania> czyli wyniki dopasowania do fragmentu dla wszystkich autorow, przydatne raczej do debugu 
