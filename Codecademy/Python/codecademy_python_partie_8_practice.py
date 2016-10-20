# Partie 8 :
# Practice Makes Perfect
# Practice! Practice Practice!

# test si un chiffre/nombre est paire ou impaire (is even  vs odd number ?)
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
	
#test si un chiffre/nombre est entier (is int ?)	
def is_int(x):
    if int(x) == x:
        return True
    else:
        return False

#test digit_sum : faire la somme des chiffres composants un nombre passé en paramètre dans la fonction		
def digit_sum(n):
    chaine = str(n)
    total = 0
    for chiffre in chaine:
        total += int(chiffre)
    return total

# calculer le factoriel
def factorial(x):
    total = 0
    for i in range(x,0,-1):
        print i
        if x == i:
            total += x
        else:
            total = total * i
    return total

factorial(2)

# tester si c'est un nombre premier (prime number)
"""
def is_int(x):
    if int(x) == x:
        return True
    else:
        return False

def is_prime(x):
    if x > 1:
        if x == 2:
            return True
        else:
            marq = 0
            for i in range(2,x,1):
                test = float(x) / i
                if is_int(test):
                    marq += 1
            if marq > 0:
                return False
            else:
                return True
    else:
        return False
        
print is_prime(4)
"""
def is_prime(x):
    if x < 2:
        return False
    else:
        i = 2
        while i < x:
            if x % i == 0:
                return False
            i += 1
    return True
	
# inverser l'ordre des lettres d'une chaine de caractère

def reverse(test):
    stringreverse = ""
    for i in range(len(test),0,-1):
        print i
        stringreverse += test[i-1]
        #print stringreverse
    return stringreverse
    
reverse("abcd")

# enlever / supprimer les voyelles d'une chaine de caractère
"""
def anti_vowel(text):
    wvowel = ""
    vowel = ["a","e","i","o","u"]
    for i in range(len(text)):
        test = 0
        for vo in vowel:
            if text[i].lower() == vo.lower():
                test += 1
        if test == 0:
            wvowel += text[i]
    return wvowel

print anti_vowel("test")
"""
def anti_vowel(text):
    wvowel = ""
    vowel = "aeiou"
    for i in range(len(text)):
        if text[i].lower() not in vowel:
            wvowel += text[i]
            
    return wvowel

print anti_vowel("test")



# calculer le score (sum / somme) à partir d'un dictionnaire de valeur
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    somme = 0
    for i in range(len(word)):
        print i
        for let in score:
            print let
            if word[i].lower() == let:
                somme += score[let]

    return somme

print scrabble_score("test")	


# remplacer une chaine de caractère passée en paramètre dans une autre chaine
def censor(text,word):
    textsplit = text.split()
    textreturn = ""
    listsp = []
    for sp in textsplit:
        if sp.lower() == word.lower():
            listsp.append("*" * len(sp))
        else:
            listsp.append(sp)
        
    textreturn = " ".join(listsp)
        
    return textreturn

print censor("hey hey","hey")


# compter le nombre d'occurence dans une chaine ou une liste
def count(sequence,item):
    nb = 0
    for seq in sequence:
        if seq == item:
            nb += 1
    return nb
    
print count("aabbac","a")
print count("aabbac",1)
print count([1,2,1,1],1)
print count(["1","2","1","1"],1)
print count([1,2,1,1],"1")
print count(["1","2","1","1"],"1")


# supprimer les nombres paires d'une liste de nombre (delete if is even)
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def purify(liste):
    listereturn = liste
    i = 0
    while i < len(listereturn):
        print "i"
        print i
        if is_even(liste[i]) == False:
            print "liste i"
            print liste[i]
            listereturn.remove(liste[i])
            print "liste retour"
            print listereturn
        else:
            i += 1
    return listereturn

print purify([1,2,3,4,5,6,7,8,9,10,11,12])
 
 #produit d'une liste de nombre
 def product(listenb):
    total = 1
    for nb in listenb:
        total *= nb
    return total
	

# supprimer les doublons dans une liste

def remove_duplicates(texte):
    textereturn = []
    for lettre in texte:
            if lettre not in textereturn:
                textereturn.append(lettre)
    return textereturn

print remove_duplicates([1,1,2,2])


# retourner le milieu d'une liste
from math import *

def median(listenb):
    medianreturn = 0
    listesorted = sorted(listenb)
    #print listesorted
    if len(listesorted) % 2 != 0:
        milieusup = int(ceil(len(listesorted)/2))
        print "milieusup"
        print milieusup
        medianreturn = listesorted[milieusup]
    else:
        milieusup = int(ceil(len(listesorted)/2))
        milieuinf = milieusup - 1
        moyenne = float((listesorted[milieusup]+listesorted[milieuinf]))/2
        medianreturn = moyenne
    
    return medianreturn
    
print median([5, 2, 3, 1, 4])

