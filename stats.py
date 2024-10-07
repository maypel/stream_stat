import random

def generate_random_sets(n):
    random_sets = []
    for _ in range(n):
        random_set = random.sample(range(1, 50), 5)
        random_sets.append(random_set)
    return random_sets

# Exemple : Générer 5 ensembles aléatoires de 8 chiffres
n = 5
sets = generate_random_sets(n)

for i, s in enumerate(sets):
    print(f"Ensemble {i+1}: {s}")

