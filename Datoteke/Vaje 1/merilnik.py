import time                         # Štoparica

import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov
from zabica import zabica 
from zabica import zabica_iteracija
def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""
    # NAMIG: klic funkcije `time.perf_counter()` vam vrne število sekund od 
    # neke točke v času. Če izmerite čas pred izračunom funkcije in čas po 
    # končanem izračunu, vam razlika časov pove čas izvajanja (funkcija je 
    # natančnejša od time.time()).
    zacetek = time.perf_counter()
    fun(primer)
    konec = time.perf_counter()
    #raise NotImplementedError
    return konec - zacetek


def oceni_potreben_cas(fun, gen_primerov, n, k):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `gen_primerov(n)`, in vzame povprečje časa za `k` primerov. """

    # NAMIG: `k`-krat generirajte nov testni primer velikosti `n` s klicem
    # `gen_primerov(n)` in izračunajte povprečje časa, ki ga funkcija porabi za
    # te testne primere.
    zac = time.perf_counter()
    for _ in range(k):
        fun(gen_primerov(n))
    konc = time.perf_counter()
    return (konc - zac) / k
    #raise NotImplementedError


def narisi_in_pokazi_graf(fun, gen_primerov, sez_n, k=10):
    """ Funkcija nariše graf porabljenega časa za izračun `fun` na primerih
    generiranih z `gen_primerov`, glede na velikosti primerov v `sez_n`. Za
    oceno uporabi `k` ponovitev. """

    # NAMIG: preprost graf lahko narišemo z `plt.plot(sez_x, sez_y, 'r')`, ki z
    # rdečo črto poveže točke, ki jih definirata seznama `sez_x` in `sez_y`. Da
    # se graf prikaže uporabniku, uporabimo ukaz `plt.show()`. Za lepše grafe
    # si poglejte primere knjižnice [matplotlib.pyplot] (ki smo jo preimenovali
    # v `plt`).
    sez_x, sez_y = [], []
    for el in sez_n:
        sez_x.append(el)
        sez_y.append(oceni_potreben_cas(fun, gen_primerov, el, k))
    
    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.xlabel('Velikost problema.')
    plt.ylabel('Potreben cas [s]')
    plt.plot(sez_x, sez_y, 'r')
    plt.show()


def izpisi_case(fun, gen_primerov, sez_n, k=10):
    """ Funkcija izpiše tabelo časa za izračun `fun` na primerih generiranih z
    `gen_primerov`, glede na velikosti primerov v `sez_n`. Za oceno uporabi `k`
    ponovitev. """

    # Seznam časov, ki jih želimo tabelirati
    casi = []
    for el in sez_n:
        casi.append(oceni_potreben_cas(fun, gen_primerov, el, k))
    
    # za lepšo poravnavo izračunamo širino levega stolpca
    maks = max(sez_n)
    pad = len(str(maks)) + 1 # DOPOLNITE KODO
    # izpiši glavo tabele
    """ POJASNILO: če uporabimo `{:n}` za f-niz, bo metoda vstavila
    argument, in nato na desno dopolnila presledke, dokler ni skupna dolžina
    niza enaka vrednosti `n`. Če želimo širino prilagoditi glede na neko
    spremenljivko, to storimo kot prikazuje spodnja vrstica (torej s
    `{:{pad}}` kjer moramo nato podati vrednost za `pad`)."""
    print("{:{pad}} | Čas izvedbe [s]".format("n", pad=pad))
    # horizontalni separator
    sep_len = len(str(max(casi))) + pad + 2  # DOPOLNITE KODO (črta naj bo široka kot najširša vrstica)
    print("-"*sep_len)

    # izpiši vrstice
    for i in range(len(sez_n)):
        razmik = ' '*(pad - len(str(sez_n[i]))+1)
        print(str(sez_n[i]) + razmik + '| ' + str(casi[i]))
    
    # končna tabela naj izgleda približno takole (seveda pa jo lahko polepšate):
    # n  | Čas izvedbe [s]
    # ---------------------------
    # 10 | 4.198900114715798e-06 
    # 20 | 1.6393299847550225e-05
    # 30 | 3.7693600006605266e-05

    #raise NotImplementedError

def primerjaj_case_dveh(fun1, fun2, gen_primerov, sez_n, k=10):
    """ Funkcija izpiše tabelo časa za izračun 'fun1' in 'fun2' na primerih generiranih z
    `gen_primerov`, glede na velikosti primerov v `sez_n`. Za oceno uporabi `k`
    ponovitev. Funkcija tudi nariše graf kjer še lažje opazimo razliko med delovanjem funkcijama. """

    # Seznam časov, ki jih želimo tabelirati
    casi1, casi2 = [], []
    for el in sez_n:
        casi1.append(oceni_potreben_cas(fun1, gen_primerov, el, k))
        casi2.append(oceni_potreben_cas(fun2, gen_primerov, el, k))
    
    # za lepšo poravnavo izračunamo širino levega stolpca
    maks = max(sez_n)
    pad = len(str(maks)) + 1 # DOPOLNITE KODO
    # izpiši glavo tabele
    
    print("{:{pad}} | Čas izvedbe[s](fun1)   | Čas izvedbe[s](fun2)".format("n", pad=pad))
    
    # horizontalni separator
    sep_len = len(str(max(casi1))) + len(str(max(casi2))) + pad + 8  # DOPOLNITE KODO (črta naj bo široka kot najširša vrstica)
    print("-"*sep_len)

    # izpiši vrstice
    for i in range(len(sez_n)):
        razmik1 = ' '*(pad - len(str(sez_n[i]))+1)
        print(str(sez_n[i]) + razmik1 + '| ' + str(casi1[i]) + razmik1 + '| ' + str(casi2[i]))
        
    #Izris grafa.
    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.plot(sez_n, casi1, label = 'Funkcija 1')        
    plt.plot(sez_n, casi2, label = 'Funkcija 2') 
    plt.xlabel('Velikost problema.')
    plt.ylabel('Potreben cas [s]')
    plt.title('Primerjava časovne zahtevnosti dveh funkcij.')
    plt.legend()
    plt.show()
    
    #Dobljen graf lahko shranimo.
    #plt.savefig('primerjava.pdf')

# -----------------------------------------------------------------------------
# Nekaj hitrih testnih funkcij


def test_gen_sez(n):
    """Generira testni seznam dolžine n."""
    return [random.randint(1, n) for _ in range(n)]

def ure_gen_sez(n):
    "Generiramo urejen seznam dolžine n."
    return [i for i in range(n)]

# -----------------------------------------------------------------------------
# Ker je datoteka mišljena kot knjižnica, imejte vse 'primere izvajanja'
# zavarovane z `if __name__ == '__main__':`, da se izvedejo zgolj če datoteko
# poženemo in se ne izvedejo če datoteko uvozimo kot knjižnico.
if __name__ == '__main__':
    #print(f'Ocene potrebnih časev funkcije kvadratične časovne zahtevnosti: {oceni_potreben_cas(test_fun_kvad, test_gen_sez,100,10)}')
    #print(narisi_in_pokazi_graf(zabica_iteracija, test_gen_sez, [i for i in range(1, 30)], 10))
    print(primerjaj_case_dveh(zabica_iteracija,zabica,test_gen_sez, [i for i in range(1, 30)], 10))
