import os, fnmatch
from tknz import *

class WordBagOfOneBookClassifierWithConnectedTokens:
      
    def __findBooksPaths(self) -> list:
        result = []
        for root, dirs, files in os.walk(self.__booksRelPath):
            for name in files:
                if fnmatch.fnmatch(name, '*.txt'):
                    result.append(os.path.join(root, name))
        return result
    
    def __buildTokenDict(self, path) -> dict:
        '''
        Builds anew or expands book's or author's word bag.
        @params:
            path     - Required : valid path to a book in txt format (Str)
        '''
        wordbag = dict()
        tokens = []

        book = open(path, 'r', encoding='utf-8')
            
        tokens = tokenize_text(book, 2)

        for word in sorted(tokens):
            wordbag[word] = wordbag.get(word, 0) + 1

        return wordbag
    
    def __buildTokenSet(self, frag) -> list:
        '''
        Builds token set for specified text.
        @params:
            frag     - Required : literary work fragment for analysis (Str)
        '''
        tokens = tokenize_frag(frag, 2)

        return tokens
    
    def __buildBooksWB(self) -> None:
        self.__booksWB = dict()
        
        paths = self.__findBooksPaths()

        for p in paths:
            dtidx = p.index('.', len(self.__booksRelPath)+1)
            title = p[len(self.__booksRelPath)+1:dtidx]
            self.__booksWB[title] = self.__buildTokenDict(p)
            self.books.append(title)
    
    def __buildClassifier(self) -> None:
        self.__bookScore = dict()

        for book in self.__booksWB:
            self.__bookScore[book] = self.__bookScore.get(book, 0)
    
    def __clearScore(self) -> None:
        for book in self.books:
            self.__bookScore[book] = 0
    
    def __prepareClassification(self, frag) -> None:
        self.__clearScore()
        fragtokens = self.__buildTokenSet(frag)
        
        for book in self.__booksWB:
            for token in fragtokens:
                self.__bookScore[book] += self.__booksWB[book].get(token, 0)
                
    def classifyFullProb(self, frag) -> dict:
        self.__prepareClassification(frag)
        result = dict()
        total = 0

        for book in self.__bookScore:
            total += self.__bookScore[book]

        if total == 0:
            total = 1

        for book in self.__bookScore:
            result[book] = self.__bookScore[book] / total

        return result
    
    def classify(self, frag) -> str:
        full = self.classifyFullProb(frag)
        maxb = ""
        maxi = 0
        for book in self.books:
            if full[book] > maxi:
                maxi = full[book]
                maxb = book

        return maxb
      
    def __init__(self, booksRelPath) -> None:
        self.books = []
        self.__booksRelPath = booksRelPath
        
        self.__buildBooksWB()
        self.__buildClassifier()