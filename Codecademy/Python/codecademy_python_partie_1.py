"""
Partie 1 : Python Syntax
"""
"""
Variables and Data Types
"""

#afficher du contenu
print "Bienvenue dans le langage Python !"

# Variable affectation
my_variable = 10

# Affectez aux variables les valeurs listées dans les instructions
my_int = 7
my_float = 1.23
my_bool = True

# mon_int contient la valeur 7 ci-dessous. Que pensez-vous
# qu'il se passera si nous lui affectons la valeur 3
# et que nous affichons le résultat ?

my_int = 7

# Changer la valeur de mon_int de 7 à 3 à la ligne 9 !

my_int = 3


# Voici le code qui écrira le contenu de mon_int dans la console : 
# Le mot clé print sera expliqué en détail très bientôt !

print my_int

"""
Whitespaces and Statements
"""

# probleme d'indentation
def spam():
oeufs = 12
return oeufs
        
print spam()

# indentation corrigée et correcte
def spam():
    oeufs = 12
    return oeufs
        
print spam()

spam = True
eggs = False

"""
Maths
"""

# Affectez la valeur 1 plus 2 à la variable compter à la ligne 3 !
count_to = 13+12

print count_to

# En utilisant une puissance, affectez 100 à oeufs à la ligne 3!

eggs = 10**2

print eggs

# Affectez la valeur 1 à jambon en utilisant un modulo a la ligne 3 !

spam = 5 % 2

print spam

#un commentaire
monty = True
python = 1.234
monty_python = python ** 2
