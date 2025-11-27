#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s: str) -> list:
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    tuples = []
    count  = 0
    for i in range(len(s)):
        if s[i] == s[i-1]:
            count += 1
        else: 
            tuples.append((s[i-1], count))
            count = 1
    tuples.append((s[-1], count))

    return tuples   


def artcode_r(s: str) -> list:
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s: 
        return []
    
    i = 1
    while i < len(s) and s[i]==s[0]:
        i +=1

    tuple_a = (s[0], i)

    return [tuple_a] + artcode_r(s[i:])

def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
