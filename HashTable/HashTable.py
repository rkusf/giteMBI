
#Creation du hash table
n = int(input("Veuillez saisir la taille de la table : "))
HashTable = [ [] for x in range(n) ]

#Fonction de hachage 
def hasher(cl):
    return (cl % len(HashTable))

#Fonction d'insertion dans la table
def inserer(cl, val, HashTable):
    Hcl = hasher(cl)
    bucket = HashTable[Hcl]
    exist = False
    for i , cl_val in enumerate(bucket):
        c, v = cl_val
        if c == cl:
            exist = True
            break
    if exist :
        bucket[i] = ((cl, val))
    else:
        bucket.append((cl, val))

#Fonction pour chercher une valeur dans la table
def chercher(HashTable, cl):
    Hcl = hasher(cl)
    bucket = HashTable[Hcl]
    for i, cl_val in enumerate(bucket):
        c, v = cl_val
        if c == cl:
            return v

#Afficher une valeur de la table
def afficher(cl):
    print(chercher(HashTable, cl))
