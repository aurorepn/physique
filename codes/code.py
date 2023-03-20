# %%

import matplotlib.pyplot as plt


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


annees = [annee for annee in range(1880, 2022)]

resDiane = [0]*142
for i in range(len(dico["Diane"])):
    resDiane[dico["Diane"][i][0] - 1880] = dico["Diane"][i][1]
plt.scatter(annees, resDiane, s=3, c="Black")
plt.show()

resMary = [0]*142
for i in range(len(dico["Mary"])):
    resMary[dico["Mary"][i][0] - 1880] = dico["Mary"][i][1]
plt.scatter(annees, resMary, s=3, c="Black")
plt.show()

resSharon = [0]*142
for i in range(len(dico["Sharon"])):
    resSharon[dico["Sharon"][i][0] - 1880] = dico["Sharon"][i][1]
plt.scatter(annees, resSharon, s=3, c="Black")
plt.show()

resJoyce = [0]*142
for i in range(len(dico["Joyce"])):
    resJoyce[dico["Joyce"][i][0] - 1880] = dico["Joyce"][i][1]
plt.scatter(annees, resJoyce, s=3, c="Black")
plt.show()

resTaylor = [0]*142
for i in range(len(dico["Taylor"])):
    resTaylor[dico["Taylor"][i][0] - 1880] = dico["Taylor"][i][1]
plt.scatter(annees, resTaylor, s=3, c="Black")
plt.show()

resMargaret = [0]*142
for i in range(len(dico["Margaret"])):
    resMargaret[dico["Margaret"][i][0] - 1880] = dico["Margaret"][i][1]
plt.scatter(annees, resMargaret, s=3, c="Black")
plt.show()

resHelen = [0]*142
for i in range(len(dico["Helen"])):
    resHelen[dico["Helen"][i][0] - 1880] = dico["Helen"][i][1]
plt.scatter(annees, resHelen, s=3, c="Black")
plt.show()



# %%
