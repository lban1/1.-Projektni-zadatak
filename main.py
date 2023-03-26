#Definiranje datuma

from datetime import date


#Definiranje rijecnika "Korisnik"

korisnik = {}


#Upis trazenih podataka od korisnika

korisnik['ime']=input('Unesite ime korisnika: ')
korisnik['ime']=korisnik['ime'].strip()
korisnik['ime']=korisnik['ime'].capitalize()

korisnik['prezime']=input('Unesite prezime korisnika: ')
korisnik['prezime']=korisnik['prezime'].strip()
korisnik['prezime']=korisnik['prezime'].capitalize()

korisnik['tel']=int(input('Unesite telefonski broj korisnika: '))


korisnik['email']=input('Unesite e-mail korisnika: ')
korisnik['email']=korisnik['email'].strip()


#Definiranje rijecnika "Artikli"

artikl = {}


#Upis trazenih podataka od korisnika

artikl['naslov']=input('Unesite naslov prodajnog artikla: ')
artikl['naslov']=artikl['naslov'].strip()
artikl['naslov']=artikl['naslov'].capitalize()

artikl['opis']=input('Unesite svoj opis prodajnog artikla: ')

artikl['cijena']=float(input('Unesite cijenu prodajnog artikla (EUR): '))

#Definiranje rijecnika "Artikli"

prodaja = {}


#Upis trazenih podataka od korisnika

dan_isteka_prodaje=int(input('Unesite dan isteka prodaje artikla: '))


#Provjera ispravnosti upisa
while dan_isteka_prodaje > 31:
    print('Pogreska unosa, pokusajte ponovo: ')
    dan_isteka_prodaje=int(input())
    if dan_isteka_prodaje <= 31:
        break

#Upis trazenih podataka od korisnika

mjesec_isteka_prodaje=int(input('Unesite mjesec isteka prodaje artikla: '))

#Provjera ispravnosti upisa
while mjesec_isteka_prodaje > 12:
    print('Pogreska unosa, pokusajte ponovo: ')
    mjesec_isteka_prodaje = int(input())
    if mjesec_isteka_prodaje<=12:
        break

#Upis trazenih podataka od korisnika

godina_isteka_prodaje=int(input('Unesite godinu isteka prodaje artikla: '))


#Definiranje datuma od unesenih podataka

prodaja['datum']=date(godina_isteka_prodaje, mjesec_isteka_prodaje, dan_isteka_prodaje)


#Upisivanje rijecnika u rijecnik iz kojeg se cita

prodaja['artikl']=artikl
prodaja['korisnik']=korisnik


#Ispis unesenih podataka oglasa

print('Informacije o prodajnom artiklu:')
print('\t Naslov:', prodaja['artikl']['naslov'])
print('\t Opis:', prodaja['artikl']['opis'])
print('\t Cijena:', prodaja['artikl']['cijena'],'EUR')

print('Datum isteka prodaje artikla:')
print('\t Dan:', prodaja['datum'].day)
print('\t Mjesec:', prodaja['datum'].month)
print('\t Godina:', prodaja['datum'].year)

print('Informacije o korisniku:')
print('\t', prodaja['korisnik']['prezime'], prodaja['korisnik']['ime'])
print('\t Telefon:', prodaja['korisnik']['tel'])
print('\t E-mail:', prodaja['korisnik']['email'])