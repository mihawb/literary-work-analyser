import os, fnmatch
import pandas as pd

class TxtDocMatrixClassifier:
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

    def __buildFragDict(self, frag) -> None:
        frag = frag.replace('\n', ' ')
        for char in self.__unnecessary_chars:
            frag = frag.replace(char, '')
        frag = frag.strip().lower().split()

        self.__fragTokens = dict()
        for token in frag:
            if token not in self.__stops:
                self.__fragTokens[token] = self.__fragTokens.get(token, 0) + 1
        self.__fragTokens = dict(sorted(self.__fragTokens.items(), key=lambda x: x[1], reverse = True))

    def __buildTDMfromFrag(self) -> None:
        self.__fragTDM = pd.DataFrame(columns=self.authors)
        for ft in self.__fragTokens:
            licznik = [0] * len(self.authors)
            for i, author in enumerate(self.authors):
                for token in self.__authorsWB[author]:
                    if ft == token:
                        licznik[i] += self.__authorsWB[author][token]
            element = pd.DataFrame([licznik], columns=self.authors, index=[ft])
            self.__fragTDM = self.__fragTDM.append(element)
        
    def classifyFullProb(self, frag) -> dict:
        self.__buildFragDict(frag)
        self.__buildTDMfromFrag()
        
        result = dict()
        for i, el in enumerate(self.__fragTDM.sum()):
            result[self.authors[i]] = el
            
        return result

    def classify(self, frag) -> str:
        full = self.classifyFullProb(frag)
        maxa = ""
        maxi = 0
        for author in full:
            if full[author] > maxi:
                maxi = full[author]
                maxa = author
        return maxa
    
    def getAuthors(self) -> list:
        return self.authors
    
#     def getAuthWB(self):
#         return self.__authorsWB
    
#     def getFragDict(self):
#         return self.__fragTokens

#     def getTDM(self):
#         return self.__fragTDM

    def __init__(self, bookRelPath, lim) -> None:
        self.__booksRelPath = bookRelPath
        self.__authorsWB = dict()
        self.__lim = lim

        self.__buildAuthorsWB()
        self.authors = list(self.__authorsWB.keys())
