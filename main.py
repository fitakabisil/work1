chaine = input("ecrivez votre phrase")  #chaine est la variable qui va representer le 'string' original
liste_de_mots = chaine.split()  #le code split() va transformer la chaine(string) en une liste.
nombre_de_mots = len(liste_de_mots)  #de ce que j'ai compris, len() va transformer la liste en 'string'
print(nombre_de_mots)  #ceci est la sortie (output)