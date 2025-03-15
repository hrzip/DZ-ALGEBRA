
potrosnja_na_100km = float(input('Kolika je potrošnja automobila na 100km ? '))
cijena_po_litri = float(input('Kolika je cijena benzina po litri ? '))


udaljenost_u_oba_smjera = float(input('kolika je udaljenost u oba smjera ukupno ? '))
BROJ_DANA_U_MJESECU = int(input('Za koliko dana u mjesecu želite izračunati ? '))


trosak_po_km = (potrosnja_na_100km / 100) * cijena_po_litri

mjesecni_trosak = trosak_po_km * udaljenost_u_oba_smjera * BROJ_DANA_U_MJESECU


print('Ukupni trošak za', BROJ_DANA_U_MJESECU, 'dana je : ', mjesecni_trosak, "kn")
