
def function(str):
  for index,c in enumerate(str):    #dans cette boucle , les valeurs de "index" sont de type enier , sont (0,1,2....len(str)), et les valeur de c sont de type char , et ce sont les lettres de la chaine donnee .
    if str[:index+1].count(c) > 1:  # la , on va faire un teste s'il ya un letter qui VA se repeter plus que une fois dans les mots suivant par ordre  : str[0],str[0]str[1],str[0]str[1]str[2],...,str[0]str[1]str[2]....str[index+1] , (on a fait +1 car sinon il va arreter sur la letter juste avant la dernier car la valeur final de index est len(str) )
      return c                      # c'est la letter retourné par la fonction
  return "NULL"                     #si n'ya aucune lettre qui se reppete retourner NULL

print(function("ABBCA"))
print(function("ABCCBA"))
print(function("abcd"))
