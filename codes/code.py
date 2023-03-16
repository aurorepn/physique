dico = {}

for i in range(1880, 2022):
    with open('names/yob' + str(i) + '.txt') as file:
        ligne = file.readline().split(',')
        nom = ligne[0]
        nb = int(ligne[2])
        while nb > 5:
            if nom not in dico:
                dico[nom] = []
            dico[nom].append((i, nb))
            ligne = file.readline().split(',')
            nom = ligne[0]
            nb = int(ligne[2])
#print(dico)

# dico est le dictionnaire ayant les prénoms pour clés et leur associant la liste de leurs couples d'apparition sous la forme (année, nb d'apparitions)
