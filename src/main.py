from const import FASIT
"""
Oppgave:
Iterer (gå gjennom) tallene 0-100 og print ut følgende verdier:
    - Dersom tallet kan deles på 3, print Sjoko
    - Dersom tallet kan deles på 5, print Lade
    - Dersom tallet kan deles på både 3 og 5, print SjokoLade
    - Hvis ikke, print tallet

Eksempel:
    0 : SjokoLade
    1 : 1
    2 : 2
    3 : Sjoko
    4 : 4
    5 : Lade
    15 : SjokoLade
"""


def sjoko_lade(i: int):
    """
    Din løsning her
        i = tallene fra 0-100
        return skal være 'Sjoko', 'Lade', 'SjokoLade', eller i
    """
    x = 'Resultat'

    print(f'{i}: {x}')
    return x


"""____La stå____"""
svar = ''.join(str(sjoko_lade(i)) for i in range(101))
print('Oppgaven er løst, hurra!') if svar == FASIT else print('Her er det noe feil gitt..')
