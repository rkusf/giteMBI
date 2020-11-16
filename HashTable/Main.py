
from HashTable import *
from time import *

#Test du programme
print(HashTable, end='\n')
sleep(2)

#Exemple d'insertion de valeur avec des clé déffirentes (cas où len(HashTable) = 101)
inserer(3456789, 'github', HashTable)
inserer(5467898, 'bitbucket', HashTable)

print(HashTable, end='\n')
sleep(2)

#Exemple d'insertion de valeur avec les memes valeurs de clés après le hachage   (cas où len(HashTable) = 101)
inserer(8765498, 'eclipse', HashTable)
inserer(8765599, 'qwertyvsazerty', HashTable)
inserer(8765599, 'HUNTERXHUNTER', HashTable)

print(HashTable, end='\n')
sleep(2)

afficher(8765599) 