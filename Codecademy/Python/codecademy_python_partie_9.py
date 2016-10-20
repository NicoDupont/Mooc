# Partie 9 :
# Exam Statistics
# Let's look at those grades!

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades:", grades

# imprimer 1 valeur de la liste par ligne (mettre nb, (la virgule en +) pour tout afficher sur la meme ligne)
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(liste):
    for nb in liste:
        print nb

print_grades(grades)

print "Let's compute some stats!"


# faire la somme de la liste
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(listenb):
    total = 0
    for nb in listenb:
        total += nb
    return total

print grades_sum(grades)

# fonction moyenne

def grades_average(listenb):
    return grades_sum(listenb)/float(len(listenb))
    
print grades_average(grades)


# calcul variance 

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
    
def grades_variance(grades):
    average = grades_average(grades)
    variance = 0
    for grade in grades:
        variance += (average - grade) ** 2 
    variance = variance / float(len(grades))
    return variance

print grades_variance(grades)


# calcul Standard Deviation = racine carré de la variance

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
    
def grades_variance(grades):
    average = grades_average(grades)
    variance = 0
    for grade in grades:
        variance += (average - grade) ** 2 
    variance = variance / float(len(grades))
    return variance

print grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)
