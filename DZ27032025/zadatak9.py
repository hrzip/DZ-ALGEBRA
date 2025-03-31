# Napravite listu s pet filmova koje želite pogledati i listu sa pet filmova koje ste već pogledali. Zatim napravite novu listu koja će sadržavati filmove koje ste pogledali i koje biste ponovno pogledali

pogledani = ["Gospodar Prstenova", "Hachiko", "Pink Panther", "Zvjezdani ratovi", "All Quiet on the Western Front"]
zelim_pogledati = ["The Accountant 1", "The Accountant 2", "Sicario 1", "Sicario 2", "Sicario 3"]

zelim_ponovno_pogledati = pogledani[:3]
konacna_lista = zelim_ponovno_pogledati + pogledani

konacna_lista_set = set(konacna_lista) 

print(konacna_lista_set)
