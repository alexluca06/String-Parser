336CB Luca Aurel-Alexandru

	Functia "extract_states(pattern)" primeste ca parametru pattern-ul si
returneaza fiecare stare posibila a patternului respectiv sub forma unei liste
(pentru pattern-ul: LFA -> ['e', 'L','LF',...]. Lista este utilizata la formarea
matricei Delta in functia make_delta(), dat si in functia find_pattern
(pattern, text) pentru a putea accesa starea din matrice.

	Functia "make_delta(pattern)" primeste ca parametru pattern-ul si 
returneaza matricea delta. Matricea este reprezentata sub forma unui dictionar
ale carui chei sunt toate starile patternului(functia "extract_states"), chei
ale caror valori sunt tot dictionare ce au drept chei fiecare litera din alfabet,
iar ca valoare, ceea ce ne intereseaza, starea in care vom trece la intalnirea
literei respective.
Pentru completarea matricei, parcurg pattern-ul, litera cu
litera, si compar cu fiecare caracter ce ar putea aparea in pattern. Daca gasesc
o potrivire, inseamna ca pot trece intr-o stare superioara si completez pe pozitia
respectiva in matrice cu starea in care pot trece. Daca nu gasesc o potrivire, 
dar respectiva litera s-a mai gasit in pattern, incep sa caut cea mai buna stare
in care pot ajunge(elimin prima litera din pattern-ul curent(de exemplu: EZE-> ZE)
si adaug la sfarsit caracterul cu care fac comparatia(de exemplu:ZE + Z) si verific
daca "noul pattern" format il gasesc in lista de stari posibile. Tot continui sa 
elimin pana gasesc prima potrivire, fiind cea mai buna(cea mai lunga) si trec ca
stare lungimea patternului ce se potriveste).

	Functia "find_pattern(pattern, text)" primeste ca parametrii pattern-ul si
textul si scrie in fisier pozitiile la care se gaseste pattern-ul in text. Parcurge
textul litera cu litera si in functie de caracterul curent si de matricea delta,
decide daca pattern-ul apare sau nu in text.

