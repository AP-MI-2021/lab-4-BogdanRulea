
#1 citirea
def citire_lista():
    lst = []
    n = int(input("Scrie numarul de elemente din lista: ")) # citesc numarul de elemente din lista
    for i in range(n):
        element_lista = int(input(f"Scrie elementul de pe pozitia {i}: ")) #citesc fiecare element din lista
        lst.append(element_lista) #adaug elementul citit in lista finala
    
    return lst

#2 afisarea numerelor negative din lista
def afisare_numere_negative(lst : list[int]):
    lista_finala = []
    for i in lst:
        if i < 0: #verific daca numarul este negativ 
            lista_finala.append(i) #adaug numarul in lista
    
    return lista_finala

#testare 2
def test_afisare_numere_negative():
    assert afisare_numere_negative([-1,0,2,-3,5]) == [-1,-3]
    assert afisare_numere_negative([-2,3,4,-5,-9]) == [-2,-5,-9]
    assert afisare_numere_negative([2,4,5,7]) == []

test_afisare_numere_negative()
#3 cel mai mic numar cu ultima cifra egala cu o cifra citita de la tastatura
def afisareCelMaiMicNumar(lst : list[int], numarCitit : int):
    maxim =0 
    for index in lst:
        numar = index
        if numar < 0:
            numar *=-1 #daca numarul este negativ il fac pozitiv
        if numar%10 == numarCitit and (index < maxim or maxim == 0): #verific relatia din problema
            maxim = index #daca relatia este verificata retin numarul intr-o variabila ajutatoare
    return maxim

def test_afisareCelMaiMicNumar():
    assert afisareCelMaiMicNumar([1, 6, 34, 68, 40, 48, 20], 8) == 48
    assert afisareCelMaiMicNumar([2,34,56,64,8], 4) == 34
    assert afisareCelMaiMicNumar([2,3,5,6,9,19],9) == 9

#testare 3
test_afisareCelMaiMicNumar()

#4 lista cu numerele superprime

#algoritmul pentru verificarea unui numar daca este prim
def is_prime(numar : int):
    if numar < 2:
        return False
    if numar == 2:
        return True
    
    for i in range(3, numar//2 + 1):
        if numar % i == 0:
            return False
    
    return True

def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(24) == False
    assert is_prime(9) == False

test_is_prime()

def AfisareNumereSuperprime(lst : list[int]):
    lista_finala = []
    for numar in lst:
        if numar > 0:
            gasit = 1 # presupun ca numarul verificat este superprim
            numar1 = numar
            while numar1 > 0:
                if is_prime(numar1) == False: #verific daca numarul nu este prim
                    gasit = 0  #daca nu este prim inseamna ca nici numarul nu este superprim
                numar1 //=10

            if gasit == 1:
                lista_finala.append(numar)   #daca numarul este superprim il adaug in lista         

    return lista_finala

def test_AfisareNumereSuperprime():
    assert AfisareNumereSuperprime([173,239]) == [239]
    assert AfisareNumereSuperprime([233, 1235, 57, 28]) == [233]
    assert AfisareNumereSuperprime([324,2534,56534,7777]) == []

test_AfisareNumereSuperprime()

#5 inlocuirea listei initiale 


#algoritmul pentru veerificarea cmmdc
def cmmdc(numar1 : int, numar2 : int):
    while numar1 != numar2:
        if numar1 > numar2:
            numar1 -= numar2
        else:
            numar2 -= numar1
    
    return numar1

def test_cmmdc():
    assert cmmdc(6,7) == 1
    assert cmmdc(12,24) == 12
    assert cmmdc(12, 8) == 4

test_cmmdc()

#calculez cmmdc pentru toate numerele pozitive din lista
def CelMaiMareCmmdcAlNumerelorPoz(lst : list[int]):
    CelMaiMareDiv = -1

    for i in lst:
        if i > 0 and CelMaiMareDiv == -1:
            CelMaiMareDiv = i
        
        elif i>0:
            CelMaiMareDiv = cmmdc(CelMaiMareDiv, i)
    
    return CelMaiMareDiv


def ListaObtinutaDinListaInitiala(lst : list[int]):
    lista_finala = []
    cmmdc_toata_lista = CelMaiMareCmmdcAlNumerelorPoz(lst)
    for i in lst:
        if i < 0:
            numar_invers = str(i)#convertesc numarul din int in string
            numar_invers = numar_invers[1:] #elimin '-'-ul din numar
            numar_invers = numar_invers[::-1] #daca numarul este negativ inversez cifrele
            numar_invers = int("-" + numar_invers) #adaug un zero in numarul inversat ca sa il fac din nou negativ
            lista_finala.append(int(numar_invers))
        elif i>0:
            lista_finala.append(cmmdc_toata_lista) #daca numarul este pozitiv il inlocuiesc cu cmmdc numerelor pozitive 
        else:
            lista_finala.append(i)
    
    return lista_finala

def test_ListaObtinutaDinListaInitiala():
    assert ListaObtinutaDinListaInitiala([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]
    assert ListaObtinutaDinListaInitiala([-23,22,22,22,-56,-71]) == [-32, 22,22,22, -65, -17]
    assert ListaObtinutaDinListaInitiala([-23,34,-25,0]) == [-32,34,-52,0]

test_ListaObtinutaDinListaInitiala()
    
def Meniu():
    print("1. Citirea unei liste cu numere intregi.")
    print("2. Afisarea tuturor numerelor negative nenule din lista.")
    print("3. Afisarea celui mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura.")
    print("4. Afisarea tuturor numerelor superprime din lista.")
    print("5. Inlocuirea numerelor strict pozitive din lista cu cmmdc si numerele negative cu inversele lor.")
    print("x. Program incheiat.")

def main():
    Meniu()
    lst = []
    is_running = True
    while is_running:
        command = input("Scrie numarul problemei: ")
        if command == '1':
            lst = citire_lista()
        elif command == '2':
            print("Ai ales optiunea 2: Afisarea tuturor numerelor negative nenule din lista")
            print(f"Numerele negative nenule din lista {lst} sunt: {afisare_numere_negative(lst)}")
        elif command == '3':
            print("Ai ales optiunea 3: Afisarea celui mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura.")
            numar = int(input("Scrie numarul: "))
            print(f"Cel mai mic numar cu ultima cifra {numar}: {afisareCelMaiMicNumar(lst,numar)}")
        elif command == '4':
            print("Ai ales optiunea 4: Afisarea tuturor numerelor superprime din lista.")
            print(f"Numerele superprime din lista {lst} sunt: {AfisareNumereSuperprime(lst)}")
        elif command == '5':
            print("Ai ales optiunea 5: Inlocuirea numerelor strict pozitive din lista cu cmmdc si numerele negative cu inversele lor.")
            print(f"Lista rezultata din lista {lst} este: {ListaObtinutaDinListaInitiala(lst)}")
        elif command == 'x':
            print("Program incheiat!")
            is_running = False
        else:
            print("Problema inexistenta, incearca din nou: ")

main()