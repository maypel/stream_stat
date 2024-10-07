import random
import argparse
import pandas as pd
import sqlite3

def generate_random_sets(n):
    random_sets = []
    for _ in range(n):
        random_set = random.sample(range(1, 50), 5)
        random_sets.append(random_set)
    return random_sets

def main():
    parser = argparse.ArgumentParser(description="Générer des ensembles aléatoires de chiffres.")
    parser.add_argument('-n', type=int, help='Nombre d\'ensembles à générer', required=True)
    parser.add_argument('--output', type=str, choices=['dataframe', 'csv', 'sqlite'], help='Méthode de sauvegarde des résultats', required=True)
    
    args = parser.parse_args()
    n = args.n
    output = args.output

    sets = generate_random_sets(n)

    # Affichage des ensembles générés
    for i, s in enumerate(sets):
        print(f"Ensemble {i+1}: {s}")

    # Sauvegarde des résultats
    if output == 'dataframe':
        df = pd.DataFrame(sets, columns=[f'Numéro_{i+1}' for i in range(5)])
        print("DataFrame créé:")
        print(df)
    elif output == 'csv':
        df = pd.DataFrame(sets, columns=[f'Numéro_{i+1}' for i in range(5)])
        df.to_csv('random_sets.csv', index=False)
        print("Les ensembles aléatoires ont été sauvegardés dans 'random_sets.csv'.")
    elif output == 'sqlite':
        df = pd.DataFrame(sets, columns=[f'Numéro_{i+1}' for i in range(5)])
        conn = sqlite3.connect('random_sets.db')
        df.to_sql('random_sets', conn, if_exists='replace', index=False)
        conn.close()
        print("Les ensembles aléatoires ont été sauvegardés dans 'random_sets.db'.")

if __name__ == '__main__':
    main()
