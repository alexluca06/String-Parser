import sys


# Functie ce returneaza o lista cu toate starile posibile ale patternului
def extract_states(p):
    pattern_state = []
    for i in range(0, len(p)):
        pattern_state.append(pattern[0:(i - len(p))])
    # epsilon(cuvantul vid)
    pattern_state[0] = "e"
    return pattern_state


# Functie ce returneaza matricea delta
def make_delta(p):
    pattern_state = extract_states(p)
    matrix = {}
    for j in range(len(pattern_state)):
        matrix[pattern_state[j]] = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "I": 0, "J": 0, "H": 0,
                                    "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
                                    "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0
                                    }
    # indice litere in pattern
    index = 0
    for current_state in pattern_state:
        for character in matrix[current_state]:
            # litera curenta din pattern se potriveste cu cea din dictionar->avansam la o stare superioara
            if p[index] == character:
                matrix[current_state][character] = index + 1
            # litera curenta din pattern nu se potriveste cu cea din dictionar, dar a mai fost intalnita -> cautam stare
            # posibila
            elif (p[index] != character) and (character in p[0:index]):
                for j in range(len(current_state)):
                    if (current_state[j + 1: len(current_state)] + character) in pattern_state:
                        matrix[current_state][character] = len((current_state[j + 1: len(current_state)] + character))
                        break  # ne intereseaza prima optiune gasita, fiind cea mai lunga
        index = index + 1
    return matrix  # returnare matrice delta pentru pattern-ul respectiv


# Functie de cautare a unui pattern intr-un text pe baza matricei delta
def find_pattern(p, t):
    # fisierul in care va fi scris output-ul
    file = open(sys.argv[2], "w")
    # constructie lista cu toate starile patternului
    pattern_state = extract_states(p)
    q = 0
    # constructie delta
    delta = make_delta(p)
    for i in range(0, len(t) - 1):
        q = delta[pattern_state[q]][t[i]]
        if q == len(p) - 1:
            file.write(str(i - (len(p) - 2)))
            file.write(" ")
    file.write('\n')
    file.close()


if __name__ == "__main__":
    # citire text si pattern din fisier
    f = open(sys.argv[1], "r")
    pattern = f.readline()
    text = f.readline()
    f.close()
    find_pattern(pattern, text)
