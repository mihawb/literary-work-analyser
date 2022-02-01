from authorwordbag import WordBagOfAuthorClassifier
from bookwordbag import WordBagOfOneBookClassifier
from txtdocmatrix import TxtDocMatrixClassifier
from sedzia import sedzia

if __name__ == "__main__":
    # AWB potrzebuje: '..\\books', limitu
    # BWB potrzebuje: '..\\zb_uczacy'

    # a, b, f, r = sedzia(WordBagOfAuthorClassifier, '..\\books', 10, 100, 1337, 200)
    a, b, f, r = sedzia(WordBagOfOneBookClassifier, '..\\zb_uczacy', 10, 100, 1234)

    for i in range(10):
        print(a[i], r[i], a[i] == r[i], b[i])