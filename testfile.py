# this is a test file

print("jai tout change")


print("hello team!")
print("test 6")
input("comment allez vous")
print("test 4")
print("aiaiaiaiiai")
N = 1000  # on cherche les nombres premiers inférieurs à N
liste = range(N + 1)  # création de la liste des entiers de 0 à N
liste[1] = 0  # 1 n'est pas premier
nombre = 2

while nombre ** 2 <= N:  # tant que le nombre à examiner est inférieur à
    # la racine carrée de N

    liste[nombre * 2:: nombre] = [0] * ((N // nombre) - 1)  # éliminer tous les
    # multiples du nombre
    # passer au nombre non examine suivant
    nombre += 1
    while not liste[nombre]:
        nombre += 1

liste = filter(None, liste)
print(liste)  # et à la fin, on affiche le résultat