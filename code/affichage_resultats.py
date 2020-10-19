import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def sim():
    print("\n---------- Bienvenue ----------\n")

    #liste des targets, cad les choix qui s'offrent à vous
    nb_target = int(input("saisir le nombre de choix : "))
    list_target= []
    for i in range (1,nb_target+1):
        list_target.append(str(input(str(i)+"ème choix")))

    print("-------------------------------")

    #liste des paramètres
    list_params = []
    list_poids = []
    list_max_worst = []
    nb_params = int(input("saisir le nombre de paramètres : "))
    for i in range (1,nb_params+1):
        list_params.append(str(input("saisir le "+str(i)+"ème paramètre")))
        list_poids.append(float(input("donner son poids : ")))
        list_max_worst.append(int(input("voulez-vous le max ? (oui:1; non:-1) : ")))

    #création de la matrice des valeurs numériques
    mat = np.zeros((nb_target,nb_params))

    for i in range(nb_params):
        for k in range(nb_target):
            mat[k,i] = int(input(str(list_params[i])+" pour "+str(list_target[k])+" : "))

    df = pd.DataFrame(mat)
    df.index=list_target
    df.columns=list_params
    print("-------------------------------")
    print("voici votre matrice de decision : \n")
    print(df)

    #affichage du résultat de la simulation :
    print("\n-------------------------------")
    resultat_decision(mat,list_target,list_poids,list_max_worst)


def resultat_decision(mat, list_target, list_poids, list_max_worst):
    (a, b) = mat.shape

    # normalisation
    scaled = MinMaxScaler().fit_transform(mat)

    # multiplication par poids et max_worst
    for i in range(b):
        for j in range(a):
            scaled[j, i] = scaled[j, i] * list_poids[i] * list_max_worst[i]

    # somme par ligne
    somme = []
    for i in range(a):
        som = 0
        for j in range(b):
            som += scaled[i][j]
        somme.append(som)

    print("Résultats : \n")
    print(list_target)
    print(somme)
    print("\nVous devez choisir : ")
    print(list_target[somme.index(max(somme))])
