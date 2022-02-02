from authorwordbag import WordBagOfAuthorClassifier

fragment1 = 'Gdy Judym wpatrywał się coraz uważniej w to czoło zamyślone, dopiero zrozumiał, że ma przed sobą wizerunek bogini. Była to Afrodite, ona sama, która się była poczęła z piany morskiej. I mimo woli przychodziła na myśl nieskromna legenda o przyczynie onej piany wód za sprawą Uranosa. A przecież nie była to Pandemos, nie była nawet żona Hefajstówa ani kochanka Anchizesa, a tylko jasny i dobry symbol życia, córka nieba i dnia…'
fragment2 = 'Państwa-Strony będą szanowały odpowiedzialność, prawo i obowiązek rodziców lub, w odpowiednich przypadkach, członków dalszej rodziny lub środowiska, zgodnie z miejscowymi obyczajami, opiekunów prawnych lub innych osób prawnie odpowiedzialnych za dziecko, do zapewnienia mu, w sposób odpowiadający rozwojowi jego zdolności, możliwości ukierunkowania go i udzielenia mu rad przy korzystaniu przez nie z praw przyznanych mu w niniejszej konwencji.'
fragment3 = 'Siedząc już na dobrej posadzie, zdrowy, w sile wieku, przystojny „młody człowiek” postanowił ożenić się, oczywiście w kraju. Wziął tedy urlop jednomiesięczny i w czasie, którym dowolnie rozporządzał, po odtrąceniu okresu podróży, wszystko załatwił: wyszukał sobie dozgonną towarzyszkę życia, wykonał prawidłowe „konkury”, zjednał sobie przychylność rodziców, „doznał wzajemności” — (choć panna za czymś tam, czy za kimś srodze spazmowała) — wziął ślub, odbył podróż powrotną i nie spóźnił się ani o godzinę na swe stanowisko, kędyś u podnóża środkowego Uralu.'

K = WordBagOfAuthorClassifier('..\\books', 100)

print(K.classifyFullProb(fragment1))
print(K.classify(fragment1))

print(K.classifyFullProb(fragment2))
print(K.classify(fragment2))

print(K.classifyFullProb(fragment3))
print(K.classify(fragment3))